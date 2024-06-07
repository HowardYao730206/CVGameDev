
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
# imgMiku = pygame.transform.rotate(imgMiku, 90)
# imgMiku = pygame.transform.flip(imgMiku, True, False)
imgMiku = pygame.transform.rotozoom(imgMiku, 90,0.3)


#Main Loop
start = True
while start:
    #Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    #Apply Logic
    # window.fill((255,255,255))
    imgMiku = pygame.transform.smoothscale(imgMiku, (150,150))
    window.blit(imgBackground, (0,0))
    window.blit(imgMiku, (200,100))

    #Update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)