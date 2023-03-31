"""
File: point.py
"""
import random
import pygame

class Point:

    def __init__(self, x=0, y=0, size=50):
        # self ties the data to the objects scope rather than the function scope
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), size, size)
        self.color = self.random_color()

    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))