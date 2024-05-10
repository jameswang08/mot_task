from psychopy import visual, core
from random import uniform, choice, randint


class circleObj:
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

class Trial:
    def __init__(self, window, num_objects, colors, radius, trial_dur, numCues):
        #Display parameters
        self.window = window
        self.background_color = 'black'
        self.num_objects = num_objects
        self.bounds=[0,0,250] #[x, y, radius]
        self.background = visual.Circle(self.window, self.bounds[2], 100, fillColor=self.background_color, units='pix')

        #Parameters for objects
        self.objects = []
        self.colors = colors
        self.radius = radius

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
        #Display the circle containing objects
        self.background.setAutoDraw(True)
        
        #Create circle objects
        self.objects += [circleObj(self.window, self.radius, pos=[randint(-100, 100), randint(-100, 100)], 
        bounds=self.bounds, color=self.colors[i]) for i in range(self.num_objects)]
        [object.create() for object in self.objects[::-1]]

        #Display the fixation cross
        self.fixation_x.setAutoDraw(True)
        self.fixation_y.setAutoDraw(True)
        window.flip()

    def clear(self):
        pass

    def eventLoop(self):
        pass

window = visual.Window([1280, 800], allowGUI=True, monitor='test', color='white', fullscr=False)
test_trial = Trial(window, 4, ['red']*4, 20, 10, 1)
test_trial.display()
core.wait(10)
