import pygame

class Platform:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getWidth(self):
        return self.width
    def getheight(self):
        return self.height
    def getBounds(self):
        return (self.x, self.y, self.x + self.width, self.y + self.height)
    def inBounds(self, x1, y1):
        if (x1+35 >= self.x and x1+35<= self.x + self.width and y1 >= self.y and y1 <= self.y + self.height):
            return True
        return False
