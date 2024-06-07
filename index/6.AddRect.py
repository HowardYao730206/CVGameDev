
"""
Rect

    Can detect collisions with a rectangular
    Can access the x and y coordinates
    碰撞盒
    You cannot manipulate the position of the image once generated(Just like a constant)
    but with a rect, you will be able to do so

    Two ways of creating a rect
    1. pygame.Rect(x, y, width, height)
    2. surface.get_rect() #create rect around a surface/image
    Since it is a hitbox, it normally should be invisible
"""
# Import
import pygame

#initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

#Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

#Load Image
imgBackground = pygame.image.load('GreenBackground.jpg').convert()
imgMiku = pygame.image.load('scallionTransp.png').convert_alpha()
imgMiku = pygame.transform.smoothscale(imgMiku, (150,150))
rectMiku = imgMiku.get_rect()

#Rect
rectNew = pygame.Rect(500,0,200,200)

#Main Loop
start = True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    #Apply Logic
    print(rectMiku.colliderect(rectNew))
    rectMiku.x +=5
    rectMiku.y +=5
    rectNew.y += 5
    # imgMiku.x += 5 //This does not work, you cannot manipulate the position of a image

    # window.fill((255,255,255))
    window.blit(imgBackground, (0,0))
    # pygame.draw.rect(window, (0, 255, 0), rectMiku)
    pygame.draw.rect(window, (0,255, 0), rectNew)
    window.blit(imgMiku,rectMiku)

    #Update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)