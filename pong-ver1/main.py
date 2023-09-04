import pygame
from paddle import Paddle
from ball import Ball
from game_logic import move_paddle, hit_paddle

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

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

        key = pygame.key.get_pressed()
        move_paddle(key, left_paddle, right_paddle, WIDTH, HEIGHT)
        ball.move()

        hit_paddle(ball, left_paddle, right_paddle, WIDTH, HEIGHT)

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