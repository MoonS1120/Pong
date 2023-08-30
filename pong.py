import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.velocity = 5

    def draw(self):
        pygame.draw.rect(self.screen, (255 ,255, 255), (self.x, self.y, 10, 80))
    
    def move(self, up):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

class Ball:
    def __init__(self, screen, x, y, radius):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_vel = 7
        self.y_vel = 0
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen, (255 ,255, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

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
    if ball.x_vel < 0 and ball.x - ball.radius <= left_paddle.x + 10 and left_paddle.y <= ball.y <= left_paddle.y + 80:
        ball.x_vel *= -1
    elif ball.x_vel > 0 and ball.x + ball.radius >= right_paddle.x and right_paddle.y <= ball.y <= right_paddle.y + 80:
        ball.x_vel *= -1

    if ball.y - ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1

def main():
    left_paddle = Paddle(SCREEN, 15, HEIGHT//2 - 40)
    right_paddle = Paddle(SCREEN, WIDTH - 25, HEIGHT//2 - 40)
    ball = Ball(SCREEN, WIDTH//2, HEIGHT//2, 7)

    while True:
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        SCREEN.fill((0, 0, 0))
        ball.draw()

        left_paddle.draw()
        right_paddle.draw()

        input = pygame.key.get_pressed()
        move_paddle(input, left_paddle, right_paddle)
        ball.move()

        hit_paddle(ball, left_paddle, right_paddle)

if __name__ == "__main__":
    main()