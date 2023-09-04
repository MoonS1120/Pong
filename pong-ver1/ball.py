import pygame
import math

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

def bounce(ball, paddle):
    relative_d = (paddle.y + 40) - ball.y
    bounce_angle = (relative_d/40) * ((math.pi)/3)
    if ball.x_vel < 0:
        ball.x_vel = 8*math.cos(bounce_angle)
        ball.y_vel = -8*math.sin(bounce_angle)
    else:
        ball.x_vel = -8*math.cos(bounce_angle)
        ball.y_vel = -8*math.sin(bounce_angle)