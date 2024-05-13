from psychopy import visual
from random import uniform, choice, randint
import math
import numpy as np

class CircleObj:
    def __init__(self, window, radius, pos, bounds, color):
        self.window = window
        self.pos = pos
        self.radius = radius
        self.color = color
        self.velocity = [uniform(0.5, 1.5)*choice([-1,1]), uniform(0.5, 1.5)*choice([-1,1])]
        self.bounds = bounds
    
    def create(self):
        self.obj = visual.Circle(self.window, self.radius, pos=self.pos, lineColor=self.color, fillColor=self.color, units='pix')
        self.obj.setAutoDraw(True)

    def clear(self):
        self.obj.setAutoDraw(False)

    def change_color(self, new_color):
        self.color = new_color
        self.obj.setFillColor(new_color)
        self.obj.setLineColor(new_color)

    #Circle Physics
    def checkCollision(self):
        if(math.dist([0,0], self.pos) >= self.bounds[2] - self.radius):
            norm_position = np.linalg.norm(self.pos)
            normal = self.pos / norm_position
            dot_product = np.dot(self.velocity, normal)
            reflection_vector = self.velocity - 2 * dot_product * normal
            self.velocity = reflection_vector

    def move(self):
        self.checkCollision()
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.obj.setPos((self.pos[0], self.pos[1]))