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

# call character 
character = pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/character.jpg")
character_size= character.get_rect().size # get size of img
character_width = character_size[0]
character_height= character_size[1]

# for moving
character_x_pos = screen_width/2 - character_width/2 # on the half of the screen
character_y_pos = screen_height -character_height #on the bottom of screen 

# spot
to_x =0
to_y =0

# event roop 
running = True # is game on going?
while running:
    for event in pygame.event.get(): #must which event was happened?
        if event.type == pygame.QUIT: # as if push x button 
           running = False
        if event.type == pygame.KEYDOWN: #when keyboard is pushed 
            if event.key == pygame.K_LEFT:
               to_x -=5
            elif event.key == pygame.K_RIGHT:
               to_x +=5
            elif event.key == pygame.K_UP:
               to_y -=5
            elif event.key == pygame.K_DOWN:
               to_y +=5
        #when player don't push 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x 
    character_y_pos += to_y
    # limit
    if character_x_pos <0 :
        character_x_pos=0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width
     
    if character_y_pos <0 :
        character_y_pos=0
    elif character_y_pos > screen_height- character_height:
        character_y_pos = screen_height- character_height  

    screen.blit(background, (0,0)) # x, y fitting img with screen  
    screen.blit(character,(character_x_pos,character_y_pos))
    #screen.fill((134,229,127)) #with rgb 
    pygame.display.update() #keep the img while roop 
# close
pygame.quit()


