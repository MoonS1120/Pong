import pygame
import math

def move_paddle(key, left_paddle, right_paddle, HEIGHT):
    if key[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)
    elif key[pygame.K_s] and left_paddle.y + 80 + left_paddle.velocity <= HEIGHT: 
        left_paddle.move(up=False)

    if key[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)
    elif key[pygame.K_DOWN] and right_paddle.y + 80 + right_paddle.velocity <= HEIGHT:
        right_paddle.move(up=False)

def hit_paddle(ball, left_paddle, right_paddle, HEIGHT):
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