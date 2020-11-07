import pygame

pygame.init() # must to do 

# setting for screen size
screen_width = 480 
screen_height= 640
screen = pygame.display.set_mode((screen_width,screen_height)) #double


# set screen title
pygame.display.set_caption("play with me")

# bring the background img
background =pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/background.jpg")


# event roop 
running = True # is game on going?
while running:
    for event in pygame.event.get(): #must which event was happened?
     if event.type == pygame.QUIT: # as if push x button 
         running = False

    screen.blit(background, (0,0)) # x, y fitting img with screen  
    #screen.fill((134,229,127)) #with rgb 
    pygame.display.update() #keep the img while roop 
# close
pygame.quit()


