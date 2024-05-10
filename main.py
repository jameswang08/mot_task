from psychopy import visual, core
from trial import Trial

def main():
    window = visual.Window([1280, 800], allowGUI=True, monitor='test', color='white', fullscr=False)
    test_trial = Trial(window, 4, ['red']*4, 20, 10, 1)
    test_trial.display()
    core.wait(10)

if __name__ == "__main__":
    main()
