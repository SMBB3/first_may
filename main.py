import pygame
import random
import sys

pygame.init()

info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
SKY_BLUE = (135, 206, 235)

# Полноэкранный режим
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("С 1 Мая! - День Труда")
clock = pygame.time.Clock()

class Balloon:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = random.randint(1, 3)
        
    def move(self):
        self.y -= self.speed
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 30)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 30), (self.x, self.y + 60), 2)
        pygame.draw.circle(screen, WHITE, (self.x - 10, self.y - 10), 5)
        
    def is_off_screen(self):
        return self.y + 30 < 0

class Confetti:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.color = random.choice([RED, YELLOW, GREEN, BLUE, PINK, ORANGE])
        self.size = random.randint(3, 6)
        self.speed = random.randint(2, 5)
        
    def move(self):
        self.y += self.speed
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        
    def is_off_screen(self):
        return self.y > HEIGHT

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 100, WIDTH, 100))

def draw_text():
    font1 = pygame.font.Font(None, 80)
    text1 = font1.render("С ПРАЗДНИКОМ 1 МАЯ!", True, RED)
    text_rect1 = text1.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.15)))
    screen.blit(text1, text_rect1)
    
    font2 = pygame.font.Font(None, 50)
    text2 = font2.render("ДЕНЬ ТРУДА", True, BLUE)
    text_rect2 = text2.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.25)))
    screen.blit(text2, text_rect2)
    
    font3 = pygame.font.Font(None, 40)
    text3 = font3.render("Желаем успехов в труде и счастья в жизни!", True, ORANGE)
    text_rect3 = text3.get_rect(center=(WIDTH // 2, HEIGHT - 150))
    screen.blit(text3, text_rect3)
    
    font4 = pygame.font.Font(None, 60)
    text4 = font4.render("МИР! ТРУД! МАЙ!", True, RED)
    text_rect4 = text4.get_rect(center=(WIDTH // 2, HEIGHT - 70))
    screen.blit(text4, text_rect4)

def draw_clouds():
    pygame.draw.ellipse(screen, WHITE, (100, 50, 80, 50))
    pygame.draw.ellipse(screen, WHITE, (140, 30, 80, 60))
    pygame.draw.ellipse(screen, WHITE, (180, 50, 70, 50))
    
    pygame.draw.ellipse(screen, WHITE, (WIDTH - 300, 80, 70, 45))
    pygame.draw.ellipse(screen, WHITE, (WIDTH - 260, 60, 75, 55))
    pygame.draw.ellipse(screen, WHITE, (WIDTH - 220, 80, 65, 45))

def draw_sun():
    pygame.draw.circle(screen, YELLOW, (WIDTH - 100, 100), 40)

def main():
    balloons = []
    colors = [RED, BLUE, YELLOW, PINK, ORANGE]
    for i in range(6):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(HEIGHT, HEIGHT + 200)
        balloons.append(Balloon(x, y, random.choice(colors)))
    
    confettis = [Confetti() for _ in range(80)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        
        screen.fill(SKY_BLUE)
        
        draw_sun()
        draw_clouds()
        draw_ground()
        draw_text()
        
        for balloon in balloons[:]:
            balloon.move()
            balloon.draw()
            if balloon.is_off_screen():
                balloons.remove(balloon)
                balloons.append(Balloon(
                    random.randint(100, WIDTH - 100),
                    HEIGHT + random.randint(50, 150),
                    random.choice(colors)
                ))
        
        for confetti in confettis[:]:
            confetti.move()
            confetti.draw()
            if confetti.is_off_screen():
                confettis.remove(confetti)
                confettis.append(Confetti())
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()