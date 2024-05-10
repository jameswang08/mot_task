from psychopy import visual
from random import uniform, choice


class circleObj:
    def __init__(self, window, size, pos, bounds, color, shape):
        self.window = window
        self.pos = pos
        self.size = size
        self.color = color
        self.velocity = [uniform(0.5, 1.5)*choice([-1,1]), uniform(0,5, 1.5)*choice([-1,1])]
        self.bounds = bounds
    
    def create(self):
        pass

    def clear(self):
        pass

    def change_color(self, new_color):
        pass

    #Circle Physics
    def checkCollision(self):
        pass

    def move(self):
        pass

class Trial:
    def __init__(self, window, num_objects, colors, size, trial_dur, numCues):
        #Display parameters
        self.window = window
        self.background_color = 'black'
        self.num_objects = num_objects
        self.bounds=[0,0,250] #[x, y, radius]
        self.background = visual.Circle(self.window, self.bounds[2], 100, fillColor=self.background_color, units='pix')

        #Parameters for objects
        self.objects = []
        self.colors = colors
        self.size = size

        #Trial duration and number of cues per trial
        self.trial_dur = trial_dur
        self.numCues = numCues

        #Vars to determine if participant answers correctly
        self.isCue = 0
        self.response = 0

        #Fixation Cross
        self.fixation_color = 'white'
        self.fixation_x = visual.Line(self.window, start = [0, 15], end = [0, -15], lineWidth=4, units= 'pix', lineColor=self.fixation_color)
        self.fixation_y = visual.Line(self.window, start = [-15, 0], end = [15, 0], lineWidth=4, units= 'pix', lineColor=self.fixation_color)

    def display(self):
        pass

    def clear(self):
        pass

    def eventLoop(self):
        pass