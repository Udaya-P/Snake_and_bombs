from turtle import *
import random
import pygame
class Bomb(Turtle):
    def __init__(self):
        super().__init__()
        register_shape("C:\\PYTHON\\SEM-1\\Snakegame\\bbomb.gif")
        self.penup()
        self.shapesize(stretch_len = 1.5, stretch_wid=1.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def play_sound(sound):
        pygame.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()


