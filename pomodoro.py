import time
import os
import pygame

# use to make arguments
from sys import argv

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
    strInput = input("Type 'w' to set work timer, 'b' to set break timer, or 'exit' to exit: ").lower()

    if (strInput == "w"):
        try:
            inputTime = float(input("Set work timer for 'x' minutes (or press enter to set to 25 minutes): "))
        except:
            inputTime = 25

        countdown(inputTime, "Work")
    elif (strInput == "b"):
        try:
            inputTime = float(input("Set break timer for 'x' minutes (or press enter to set to 5 minutes): "))
        except:
            inputTime = 5

        countdown(inputTime, "Break")
    elif (strInput == "exit" or strInput == "e"):
        os.system("clear")
        exit()
    else:
        newInput()

def countdown(inputTime, strStatus):
    # convert inputted time in minutes to total seconds
    t = inputTime * 60

    # print time remaining as string formatted to mm:ss
    while (t > 0):
        os.system("clear")
        print(strStatus + " time:")

        minutes = str(int(t / 60)).zfill(2)
        seconds = str(int(t % 60)).zfill(2)
        
        print(minutes + ":" + seconds)
        time.sleep(1)
        t -= 1
    
    finished()

def finished():
    print("Timer done.")
    
    # initialize pygame
    pygame.init()
    
    # initialize pygame mixer to alarm.wav
    s = pygame.mixer.Sound("alarm.wav")
    
    # play audio on loop until input
    s.play(-1)
    input("Press 'Enter' to stop alarm.")
    s.stop()

    # new input
    os.system("clear")
    newInput()

welcome()
