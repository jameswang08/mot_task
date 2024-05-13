from psychopy import visual, core, event
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
    window = visual.Window([1280, 800], allowGUI=True, monitor='test', color='white', fullscr=False)
    test_trial = Trial(window, 4, ['blue']+['red']*3, 20, 10, 1)
    test_trial.display()
    test_trial.eventLoop()
    core.wait(10)

if __name__ == "__main__":
    main()
