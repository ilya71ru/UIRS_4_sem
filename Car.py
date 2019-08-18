import math
import random
#from Road import TRoad
import pygame
from Lazer import Lazer


class TCar:

    def __init__(self, x, y, v, angle):
        self.x = x
        self.y = y
        self.dx_error = 0
        self.dy_error = 0
        self.v = v
        self.angle = angle
        self.isLive = True
        self.arr_laser = [Lazer(0), Lazer(math.pi/4), Lazer(-math.pi/4), Lazer(math.pi/2), Lazer(-math.pi/2)]

    def move(self, step, carrect: pygame.Rect, PictureArr, sc):
        """Изменение координат машинки"""
        if self.isLive:
            dx = self.v * math.cos(self.angle)*step
            dy = -self.v * math.sin(self.angle)*step
            self.dx_error += dx - int(dx)
            self.dy_error += dy - int(dy)
            self.x += dx
            self.y += dy
            if abs(self.dx_error)>=1:
                dx+=int(self.dx_error)
                self.dx_error-=int(self.dx_error)
            if abs(self.dy_error)>=1:
                dy+=int(self.dy_error)
                self.dy_error-=int(self.dy_error)

            carrect.move_ip(dx, dy)
            distance = []
            for laser in self.arr_laser:
                distance.append(laser.move(PictureArr, self, sc))
        return distance


    def turn_left(self, phi=math.pi/13.0):
        """Поворот вектора скорости против часовой стрелки на угол phi"""
        self.angle += phi
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

    def turn_right(self, phi=math.pi/13.0):
        """Поворот вектора скорости по часовой стрелки на угол phi"""
        self.angle -= phi
        if self.angle < 0:
            self.angle += 2 * math.pi