import pygame

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