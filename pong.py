import pygame
import math
from sys import exit

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

class Paddle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.velocity = 6

    def draw(self):
        pygame.draw.rect(self.screen, (255 ,255, 255), (self.x, self.y, 10, 80))
    
    def move(self, up):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    def __init__(self, screen, x, y, radius):
        self.screen = screen
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.x_vel = 4
        self.y_vel = 0
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen, (255 ,255, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel *= -1
        self.y_vel = 0

def move_paddle(input, left_paddle, right_paddle):
    if input[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)
    elif input[pygame.K_s] and left_paddle.y + 80 + left_paddle.velocity <= HEIGHT: 
        left_paddle.move(up=False)

    if input[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)
    elif input[pygame.K_DOWN] and right_paddle.y + 80 + right_paddle.velocity <= HEIGHT:
        right_paddle.move(up=False)

def hit_paddle(ball, left_paddle, right_paddle):
    if ball.x - ball.radius <= left_paddle.x + 10 and left_paddle.y <= ball.y <= left_paddle.y + 80:
        bounce(ball, left_paddle)
    elif ball.x + ball.radius >= right_paddle.x and right_paddle.y <= ball.y <= right_paddle.y + 80:
        bounce(ball, right_paddle)

    if ball.y - ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1

def bounce(ball, paddle):
    relative_d = (paddle.y + 40) - ball.y
    bounce_angle = (relative_d/40) * ((math.pi)/3)
    if ball.x_vel < 0:
        ball.x_vel = 8*math.cos(bounce_angle)
        ball.y_vel = -8*math.sin(bounce_angle)
    else:
        ball.x_vel = -8*math.cos(bounce_angle)
        ball.y_vel = -8*math.sin(bounce_angle)

def main():
    left_paddle = Paddle(SCREEN, 10, HEIGHT//2 - 40)
    right_paddle = Paddle(SCREEN, WIDTH - 20, HEIGHT//2 - 40)
    ball = Ball(SCREEN, WIDTH//2, HEIGHT//2, 7)
    left_score = 0
    right_score = 0

    while True:
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        SCREEN.fill((30, 30, 30))
        left_score_txt = font.render(f"{left_score}", True, (255, 255, 255))
        right_score_txt = font.render(f"{right_score}", True, (255, 255, 255))
        SCREEN.blit(left_score_txt, (WIDTH//4 - left_score_txt.get_width()//2, 20))
        SCREEN.blit(right_score_txt, (WIDTH*3//4 + right_score_txt.get_width()//2, 20))
        pygame.draw.line(SCREEN, (80, 80, 80), (WIDTH//2, 0), (WIDTH//2, HEIGHT), width=3)
        ball.draw()
        left_paddle.draw()
        right_paddle.draw()

        input = pygame.key.get_pressed()
        move_paddle(input, left_paddle, right_paddle)
        ball.move()

        hit_paddle(ball, left_paddle, right_paddle)

        if ball.x <= 0:
            right_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
        elif ball.x >= WIDTH:
            left_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()

if __name__ == "__main__":
    main()