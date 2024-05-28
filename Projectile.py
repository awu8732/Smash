import pygame

class Projectile:
    def __init__(self, vel, image):
        self.x = 0
        self.y = 0
        self.vel = vel
        self.image = image
    def draw(self, win, x, y):
        win.blit(self.image, (self.x, self.y))