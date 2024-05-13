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

#Trial Parameters
window = visual.Window(allowGUI=True, monitor='testMonitor', color='white', fullscr=True)
num_objects = 16
object_colors = ['blue']*2 + ['red']*14
object_size = 20
trial_duration = 10
numCues = 2

#Number of trials to run
num_trials = 2

def main():
    #Trail Data
    trial_data = []

    for _ in range(num_trials):
        displayTxt(window, "Some Instruction")
        test_trial = Trial(window, num_objects, object_colors, object_size, trial_duration, numCues)
        test_trial.display()
        test_trial.eventLoop()
        response = displayTxt(window, "Was this circle origionally blue?\n0 - No\n1 - Yes", input=True)
        trial_data += [(response, test_trial.getIsCue())]
    writeData(trial_data)

if __name__ == "__main__":
    main()
