# https://www.ponggame.org/

import time
import keyboard
import pyautogui
import win32api
import cv2

X = 1130
xPos = []
yPos = []
startTime = 0
endTime = 0
timeTaken = 0

keyboard.wait("h")
while not keyboard.is_pressed('q'):
    try:
        x, y = pyautogui.locateCenterOnScreen('ball.png', region=(780, 360, 344, 580),
                                              grayscale=True, confidence=0.8)
        endTime = time.time()
        timeTaken = endTime - startTime
        xPos.append(x)
        yPos.append(y)
        if len(xPos) == 3:
            xPos.pop(0)
            yPos.pop(0)

        startTime = time.time()
    except:
        1

    if len(xPos) == 2:
        xSpeed = (xPos[1] - xPos[0]) / timeTaken
        ySpeed = (yPos[1] - yPos[0]) / timeTaken
        if xSpeed > 0:
            xBallBoardDistance = X - x
            y = round(((xBallBoardDistance / xSpeed) * ySpeed) + yPos[1])
            win32api.SetCursorPos((X, y))