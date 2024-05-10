from psychopy import visual
from random import uniform, choice, randint

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
        pass

    def change_color(self, new_color):
        pass

    #Circle Physics
    def checkCollision(self):
        pass

    def move(self):
        pass