from Car import TCar
import math
import numpy as np
from PIL import Image


class TRoad:

    def __init__(self, arr):
        """в конструкторе создаем массив карты
        n - размер матрицы среза, arr - массив дороги"""
        self.PictureArr = []
        self.arr = arr.T
        for i in range(self.arr.shape[1]):
            self.PictureArr.append([])
            for j in range(self.arr.shape[0]):
                if self.arr[j][i] < 16000000:
                    self.PictureArr[i].append(255)
                else:
                    self.PictureArr[i].append(0)



    def check_is_live(self, car: TCar):
        """проверка жизни машинки"""
        if self.PictureArr[round(car.x)][round(car.y)] == 255:
            car.isLive = False

