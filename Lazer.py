#from Car import TCar
import math
import pygame

class Lazer:

    def __init__(self, angle):
        self.angle = angle
        self.color = (225, 0, 0)

    def move(self, PictureArr, car, sc):
        b = True
        x_l = car.x;
        y_l = car.y;
        while b:
            if PictureArr[round(x_l)][round(y_l)] == 0:
                x_l += math.cos(car.angle+self.angle)
                y_l -=math.sin(car.angle+self.angle)
            else:
                b = False
                pygame.draw.line(sc, self.color, [car.x, car.y], [x_l, y_l], 1)
        return ( (car.x - x_l) ** 2 + (car.y - y_l) ** 2) ** 0.5