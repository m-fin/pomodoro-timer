import time
import os
import pygame

def welcome():
    os.system("clear")
    print("""
The Pomodoro Technique is as follows:

1. Decide on the task to be done.
2. Set the pomodoro timer (traditionally to 25 minutes).
3. Work on the task.
4. End work when the timer rings and put a checkmark on a piece of paper.
5. If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2.
6. After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.

To learn more, click here:
https://en.wikipedia.org/wiki/Pomodoro_Technique
https://youtu.be/VFW3Ld7JO0w
""")
    newInput()

def newInput():
    strInput = input("Type 'w' to set work timer, 'b' to set break timer, or 'exit' to exit: ")
    strInput = strInput.lower()

    if (strInput == "w"):
        try:
            inputTime = float(input("Set work timer for 'x' minutes (or press enter to set to 25 minutes): "))
        except:
            inputTime = 25

        countdown(inputTime, True)
    elif (strInput == "b"):
        try:
            inputTime = float(input("Set break timer for 'x' minutes (or press enter to set to 5 minutes): "))
        except:
            inputTime = 5

        countdown(inputTime, False)
    elif (strInput == "exit" or strInput == "e"):
        os.system("clear")
        exit()
    else:
        newInput()

def countdown(inputTime, blnWork):
    t = inputTime * 60

    while (t > 0):
        os.system("clear")
        print("Work time:")

        minutes = str(int(t / 60)).zfill(2)
        seconds = str(int(t % 60)).zfill(2)
        
        print(minutes + ":"+ seconds)
        time.sleep(1)
        t -= 1
    
    finished()

def finished():
    print("Timer done.")

    pygame.init()
    s = pygame.mixer.Sound("alarm.wav")
    s.play(-1)

    input("Press enter to stop alarm.")

    s.stop()
    os.system("clear")

    newInput()

welcome()
