"""
Pygame Template

    Import
    Initialize
    Create Window
    Initialize Clock for FPS

    Loop
        Get events
            if quit
                quit pygame
        Apply Logic
        Update Display/Window
        set FPS

"""

# Import
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
# from numpy.random import random
# from random import uniform, random, choice, sample, randint
import random
import time

#initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Miku")

#Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280) # Width
cap.set(4,720) # Height

# Images
imgMiku = pygame.image.load("scallionTransp.png").convert_alpha()
rectMiku = imgMiku.get_rect()
rectMiku.x,rectMiku.y = 500,600
imgMiku2 = pygame.image.load("scallionTransp.png").convert_alpha()
rectMiku2 = imgMiku2.get_rect()
rectMiku2.x,rectMiku2.y = 1100,300
# imgMiku3 = pygame.image.load("../Resources/scallionTransp.png").convert_alpha()
# rectMiku3 = imgMiku3.get_rect()
# rectMiku3.x,rectMiku3.y = 0,0
imgMiku4 = pygame.image.load("scallionTransp.png").convert_alpha()
rectMiku4 = imgMiku4.get_rect()
rectMiku4.x,rectMiku4.y = 1100,700

# Variables
speed = 10
score = 0
startTime = time.time()
totalTime = 30

#Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetMiku():
    rectMiku.x = random.randint(100,img.shape[1]-100)
    rectMiku.y = img.shape[0]+50

def resetMiku2():
    rectMiku2.x = 1200
    rectMiku2.y = random.randint(0,img.shape[1]-700)

# def resetMiku3():
#     print(rectMiku3.x, rectMiku3.y)
#     print("collide")
#     rectMiku3.x = random.randint(100,600)
#     rectMiku3.y = -100

def resetMiku4():
        rectMiku4.x = random.randint(100,img.shape[1]-100)
        rectMiku4.y = 700

#Main Loop
start = True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    #Apply Logic
    imgMiku = pygame.transform.smoothscale(imgMiku, (110, 110))
    imgMiku2 = pygame.transform.smoothscale(imgMiku2, (110, 110))
    # imgMiku3 = pygame.transform.smoothscale(imgMiku3, (110, 110))
    imgMiku4 = pygame.transform.smoothscale(imgMiku4, (110, 110))
    timeRemain = int(totalTime - (time.time()- startTime))
    if timeRemain<0:
        window.fill((255,255,255))

        font = pygame.font.Font('Kanit-Regular.ttf', 50)
        textScore = font.render(f'Your Score: {score} !', 1, (255,50,50))
        textTime = font.render(f'Time Up!', 1, (255,50,50))
        window.blit(textTime,(530,275))
        window.blit(textScore, (450, 350))
    else:
        #OpenCV
        success, img = cap.read()
        img = cv2.flip(img,1)
        rectMiku.y -=speed-random.randint(0,5) #Move miku up
        rectMiku2.x -= speed-random.randint(0,5) # Move miku up
        # rectMiku3.x -= speed-random.randint(0,5)
        # rectMiku3.y += speed-random.randint(0,5)
        rectMiku4.x -= speed - random.randint(0, 5)
        rectMiku4.y -= speed - random.randint(0, 5)
        hands, img = detector.findHands(img,flipType=False)

        # check if ballon has reached the top without pop
        if rectMiku.y <-100:
            resetMiku()
            score-=1
            speed +=1
        if rectMiku2.x <-100:
            resetMiku2()
            score -= 1
        # if rectMiku3.x > 1280 or rectMiku3.y > 720:
        #     resetMiku3()
        if rectMiku4.x < -100 or rectMiku4.y < -100:
            resetMiku4()
            score -= 1

        if hands:
            hand = hands[0]
            x,y = hand['lmList'][8]
            if rectMiku.collidepoint(x,y):
                resetMiku()
                score += 1
                # speed -= 1
            if rectMiku2.collidepoint(x, y):
                resetMiku2()
                score += 1
                # speed += random.randint(0,3)
            # if rectMiku3.collidepoint(x, y):
            #     resetMiku3()
            #     score += 1
            #     # speed += 1
            if rectMiku4.collidepoint(x, y):
                resetMiku4()
                score += 1
                # speed -= 1

        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0,0))


        window.blit(imgMiku, rectMiku)
        window.blit(imgMiku2, rectMiku2)
        # window.blit(imgMiku3, rectMiku3)
        window.blit(imgMiku4, rectMiku4)
        font = pygame.font.Font('Kanit-Regular.ttf', 50)
        textScore = font.render(f'Score: {score}', 1, (255,50,50))
        textTime = font.render(f'Time: {timeRemain}', 1, (255,50,50))
        window.blit(textTime,(1000,35))
        window.blit(textScore, (35, 35))

    #Update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)