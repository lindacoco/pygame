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

# FPS
clock = pygame.time.Clock()

#speed
character_speed = 0.6


# Enemy
enemy = pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/enemy.jpg")
enemy_size= enemy.get_rect().size # get size of img
enemy_width = enemy_size[0]
enemy_height= enemy_size[1]

# for moving
enemy_x_pos = (screen_width /2) - (enemy_width /2) # on the half of the screen
enemy_y_pos = (screen_height /2) - (enemy_height /2)


# text
# font 
game_font = pygame.font.Font(None , 40) #default 

# total play time
total_time = 10

# start time
start_ticks = pygame.time.get_ticks() # start




# event roop 
running = True # is game on going?
while running:
    dt = clock.tick(60) # set for FPS 

    for event in pygame.event.get(): #must which event was happened?
        if event.type == pygame.QUIT: # as if push x button 
           running = False
        if event.type == pygame.KEYDOWN: #when keyboard is pushed 
            if event.key == pygame.K_LEFT:
               to_x -=character_speed
            elif event.key == pygame.K_RIGHT:
               to_x +=character_speed
            elif event.key == pygame.K_UP:
               to_y -=character_speed
            elif event.key == pygame.K_DOWN:
               to_y +=character_speed
        #when player don't push 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt


    # limit
    if character_x_pos <0 :
        character_x_pos=0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width
     
    if character_y_pos <0 :
        character_y_pos=0
    elif character_y_pos > screen_height- character_height:
        character_y_pos = screen_height- character_height  


    # collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #check collision
    if character_rect.colliderect(enemy_rect):
        print("crash!")
        running = False

    

    # drawing
    screen.blit(background, (0,0)) # x, y fitting img with screen  
    screen.blit(character,(character_x_pos,character_y_pos))
   
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))


    # timer
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000  # ms/1000 = per second

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
     # letter, True, font color 
    screen.blit(timer, (50,10))
    # time limit
    if total_time -elapsed_time <= 0 :
        print("time out")
        running = False


    #screen.fill((134,229,127)) #with rgb 
    pygame.display.update() #keep the img while roop 

#delay closing 
pygame.time.delay(2000) # 2 seconds delay

# close
pygame.quit()


