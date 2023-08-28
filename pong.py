import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

class Paddle:
    COLOUR = (255, 255, 255)
    VELOCITY = 5
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def create(self, screen):
        pygame.draw.rect(screen, self.COLOUR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

class Ball:
    COLOUR = (255, 255, 255)
    MAX_VELOCITY = 5
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    def create(self, screen):
        pygame.draw.circle(screen, self.COLOUR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def draw(screen, paddles, ball):
    screen.fill((0, 0, 0))

    for paddle in paddles:
        paddle.create(screen)

    ball.create(screen)

def collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

def paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)
    elif keys[pygame.K_s] and left_paddle.y + left_paddle.height + left_paddle.VELOCITY <= HEIGHT: 
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up=True)
    elif keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height + right_paddle.VELOCITY <= HEIGHT:
        right_paddle.move(up=False)

def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - 50, 20, 100)
    right_paddle = Paddle(WIDTH - 30, HEIGHT//2 - 50, 20, 100)
    ball = Ball(WIDTH//2, HEIGHT//2, 7)

    while True:
        draw(SCREEN, [left_paddle, right_paddle], ball)

        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        collision(ball, left_paddle, right_paddle)

if __name__ == "__main__":
    main()