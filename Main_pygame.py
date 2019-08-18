import pygame
import numpy
from Car import TCar
from Road import TRoad
from NeuralNetwork import NeuralNetwork
import math
import time
import sys

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def respawn(car: TCar):
    """Перемещение машинки в заданные координаты"""
    car.isLive = False
    car.x = 250
    car.y = 250
    car.isLive = True
    car.angle = 0






dt = 0.7
pygame.init()


GameFinish = False


def game():
    pygame.mixer.music.load('./Add/lil.mp3')
    pygame.mixer.music.play()

    size = width, height = 1260, 957

    screen = pygame.display.set_mode(size)

    BackGround = Background('./Add/bioF.jpg', [0, 0])

    screen.blit(BackGround.image, BackGround.rect)
    arr = pygame.surfarray.array2d(screen)
    car_im = pygame.image.load("./Add/car1.png")
    car_im2 = pygame.image.load("./Add/car2.png")
    carrect = car_im.get_rect(center=(250, 250))

    road = TRoad(arr)
    car = TCar(250, 250, 10, 0)
    car1 = TCar(250, 250, 10, 0)

    input_nodes = 5
    hidden_nodes = 25
    output_nodes = 2
    learning_rate = 0.1


    neural = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    neural2 = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    neural2.load()




    RIGHT = "to the right"
    LEFT = "to the left"
    STOP = "stop"
    ACCELERATE = "accelerate"
    SLOWDOWN = "slowdown"

    motion = STOP


    # для паузы вначале

    restart = False

    for k in range(5):

        if (restart==False):
            respawn(car1)
            carrect1 = car_im.get_rect(center=(250, 250))


            respawn(car)
            carrect = car_im.get_rect(center=(250, 250))
            screen.blit(BackGround.image, BackGround.rect)
            screen.blit(pygame.transform.rotate(car_im, 180), carrect)
            pygame.display.flip()

            start = True
            while (start):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            start = False
                        if event.key == pygame.K_F7:
                            pygame.mixer.music.load('./Add/lil2.mp3')
                            pygame.mixer.music.play()
                        if event.key == pygame.K_F6:
                            pygame.mixer.music.load('./Add/lil.mp3')
                            pygame.mixer.music.play()
            while car.isLive:

                screen.blit(BackGround.image, BackGround.rect)
                distance = car1.move(dt, carrect1, road.PictureArr, screen)
                road.check_is_live(car1)

                d_max = 0
                for d in distance:
                    if d > d_max:
                        d_max = d

                if d_max == 0:
                    continue

                n_distance = []
                for d in distance:
                    n_distance.append(d * 0.99 / d_max + 0.01)

                outputs = neural2.query(n_distance)
                study = numpy.argmax(outputs)

                if study == 0:
                    car1.turn_left()
                if study == 1:
                    car1.turn_right()
                # if study == 2:
                #     car.accelerate()
                # if study == 3:
                #     car.slowdown()

                screen.blit(pygame.transform.rotate(car_im2, 180+car1.angle*180/math.pi), carrect1)




                distance = car.move(dt, carrect, road.PictureArr, screen)
                road.check_is_live(car)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)

                    # Пользоцатель нажимает на клавишу
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F3:
                            car.isLive = False
                            restart = True

                        if event.key == pygame.K_F2:
                            pygame.mixer.music.pause()
                            k = True
                            while(k):
                                for vent in pygame.event.get():
                                    if vent.type == pygame.KEYDOWN:
                                        if vent.key == pygame.K_F7:
                                            pygame.mixer.music.load('./Add/lil2.mp3')
                                            pygame.mixer.music.play()
                                        if vent.key == pygame.K_F6:
                                            pygame.mixer.music.load('./Add/lil.mp3')
                                            pygame.mixer.music.play()
                                        if vent.key == pygame.K_F3:
                                            car.isLive = False
                                            restart = True
                                            k = False
                                        if vent.key == pygame.K_F1:
                                            pygame.mixer.music.unpause()
                                            k = False
                                    if vent.type == pygame.QUIT:
                                        sys.exit(0)

                        if event.key == pygame.K_F7:
                            pygame.mixer.music.load('./Add/lil2.mp3')
                            pygame.mixer.music.play()
                        if event.key == pygame.K_F6:
                            pygame.mixer.music.load('./Add/lil.mp3')
                            pygame.mixer.music.play()
                        # Figure out if it was an arrow key. If so
                        # adjust speed.
                        if event.key == pygame.K_LEFT:
                            motion = LEFT
                        if event.key == pygame.K_RIGHT:
                            motion = RIGHT
                        # if event.key == pygame.K_UP:
                        #     motion = ACCELERATE
                        # if event.key == pygame.K_DOWN:
                        #     motion = SLOWDOWN

                    # Пользователь отпускает клавишу
                    if event.type == pygame.KEYUP:
                        # If it is an arrow key, reset vector back to zero
                        if event.key == pygame.K_LEFT:
                            motion = STOP
                        if event.key == pygame.K_RIGHT:
                            motion = STOP
                        # if event.key == pygame.K_UP:
                        #     motion = STOP
                        # if event.key == pygame.K_DOWN:
                        #     motion = STOP
                study = 5
                if motion == LEFT:
                    car.turn_left()
                    study = 0
                if motion == RIGHT:
                    car.turn_right()
                    study = 1
                # if motion == ACCELERATE:
                #     car.accelerate()
                #     study = 2
                # if motion == SLOWDOWN:
                #     car.slowdown()
                #     study = 3
                d_max = 0
                for d in distance:
                    if d>d_max:
                        d_max = d

                if d_max == 0:
                    continue

                n_distance = []
                for d in distance:
                    n_distance.append(d*0.99/d_max+0.01)

                if study<5:
                    targets = numpy.zeros(output_nodes) + 0.01
                    targets[int(study)] = 0.99
                    neural.train(n_distance, targets)


                screen.blit(pygame.transform.rotate(car_im, 180+car.angle*180/math.pi), carrect)
                pygame.display.flip()
                time.sleep(0.02)
            print(k)


    #neural.save()
    #neural.load()


    for k in range(1000):
        if (restart == False):
            respawn(car)
            carrect = car_im.get_rect(center=(250, 250))
            while car.isLive:

                screen.blit(BackGround.image, BackGround.rect)
                distance = car.move(dt, carrect, road.PictureArr, screen)
                road.check_is_live(car)

                d_max = 0
                for d in distance:
                    if d > d_max:
                        d_max = d

                if d_max == 0:
                    continue

                n_distance = []
                for d in distance:
                    n_distance.append(d * 0.99 / d_max + 0.01)

                outputs = neural.query(n_distance)
                study = numpy.argmax(outputs)

                if study == 0:
                    car.turn_left()
                if study == 1:
                    car.turn_right()
                # if study == 2:
                #     car.accelerate()
                # if study == 3:
                #     car.slowdown()

                screen.blit(pygame.transform.rotate(car_im, 180+car.angle*180/math.pi), carrect)
                pygame.display.flip()
                time.sleep(0.02)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:
                            neural.save()

                        if event.key == pygame.K_F3:
                            car.isLive = False
                            restart = True

                        if event.key == pygame.K_F7:
                            pygame.mixer.music.load('./Add/lil2.mp3')
                            pygame.mixer.music.play()
                        if event.key == pygame.K_F6:
                            pygame.mixer.music.load('./Add/lil.mp3')
                            pygame.mixer.music.play()

                    if event.type == pygame.QUIT:
                        sys.exit(0)
            print(k)

            GameFinish = True






    #neural.load()


while (GameFinish == False):
    game()