from psychopy import visual, core, event, monitors
from trial import Trial
from datetime import datetime

#Helper functions

#display text to user and capture input if needed
def displayTxt(window, message, input = False, size = 1):
    txt = visual.TextStim(window, text=message, color='black',font='Helvetica', 
    units = 'deg', height=size, wrapWidth=size*50)
    txt.draw(window)
    window.flip()
    keys = None
    if not input:
        event.waitKeys()
    else:
        keys = event.waitKeys(keyList=['0', '1'])
        if keys:
            keys = int(keys[0])
    return keys

#write data to csv file
def writeData(data):
    # Get current date and time
    now = datetime.now()
    # Format as string
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = dt_string + '.csv'

    #write data to csv file
    with open(filename, 'w') as csvf:
        csvf.write('User Resopnse, Ground Truth\n')
        for datum in data:
            csvf.write(','.join(map(str, datum)) + '\n')



def main():
    #Trial Parameters
    window = visual.Window(allowGUI=True, monitor='testMonitor', color='white', fullscr=True)
    num_objects = 16
    object_colors = ['blue']*2 + ['red']*14
    object_size = 10
    trial_duration = 10
    numCues = 2

    #Number of trials to run
    num_trials = 45
        #Practice Trial
        #Practice Trial where user repeats until they get 3/4 trials correct
    while True:
        correct = 0
        num = 8
        colors = []
        nCues = 0
        for trial in range(4):
            if(trial<2):
                nCues = 1
                colors = ['blue']*1 + ['red']*7
            else:
                nCues = 2
                colors = ['blue']*2 + ['red']*6
            displayTxt(window, "Some Instruction")
            test_trial = Trial(window, num, colors, object_size, trial_duration, nCues)
            test_trial.display()
            test_trial.eventLoop()
            response = displayTxt(window, "Was this circle origionally blue?\n0 - No\n1 - Yes", input=True)
            if(test_trial.getIsCue()==response):
                correct+=1
        if(correct>=3):
            break
        else:
            displayTxt(window, "Try Again!")
            core.wait(2)


    #Trial Data
    trial_data = []

    for _ in range(num_trials):
        if(_ == 10):
            nCue = 3
            object_colors = ['blue']*3 + ['red']*13
        elif(_ == 20):
            nCue = 4
            object_colors = ['blue']*4 + ['red']*12
        elif(_ == 30):
            nCue = 5
            object_colors = ['blue']*5 + ['red']*11
        elif(_ == 40):
            nCue = 1
            object_colors = ['blue']*1 + ['red']*15

        displayTxt(window, "Some Instruction")
        test_trial = Trial(window, num_objects, object_colors, object_size, trial_duration, numCues)
        test_trial.display()
        test_trial.eventLoop()
        response = displayTxt(window, "Was this circle origionally blue?\n0 - No\n1 - Yes", input=True)
        trial_data += [(response, test_trial.getIsCue())]
    writeData(trial_data)

if __name__ == "__main__":
    main()