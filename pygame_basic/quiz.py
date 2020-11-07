# avoid flying poo
import pygame, random

pygame.init()

clock = pygame.time.Clock()

screen_width = 480
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

background =pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/background.jpg")
character = pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/character.jpg")
character_size= character.get_rect().size # get size of img
character_width = character_size[0]
character_height= character_size[1]

character_x_pos = screen_width/2 - character_width/2 # on the half of the screen
character_y_pos = screen_height -character_height #on the bottom of screen 

# spot  움직이기위해서 
to_x =0
to_y =0

#speed
character_speed = 0.6
enemy_speed = 5

# Enemy
enemy = pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/enemy.jpg")
enemy_size= enemy.get_rect().size # get size of img
enemy_width = enemy_size[0]
enemy_height= enemy_size[1]



# for moving 
enemy_x_pos = random.randint(0,(screen_width - enemy_width))  # on the half of the screen
enemy_y_pos = 0 #(screen_height /2) - (enemy_height /2)


#enemy2.pygame.draw.rect(screen, (134,229,127), (enemy_x_pos,0,50,50), 2)

game_font = pygame.font.Font(None , 40) #default 
total_time = 100

# start time
start_ticks = pygame.time.get_ticks() # start


running = True
fallen = True
while running :
    dt = clock.tick(60)

    for event in pygame.event.get(): #must which event was happened?

        if event.type == pygame.QUIT: # as if push x button 
           running = False
        if event.type == pygame.KEYDOWN: #when keyboard is pushed 
            if event.key == pygame.K_LEFT:
               to_x -=character_speed
            elif event.key == pygame.K_RIGHT:
               to_x +=character_speed
        
        
        #when player don't push 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    enemy_y_pos += enemy_speed 
    if enemy_y_pos > screen_height :
        enemy_y_pos = 0 
        enemy_x_pos = random.randint(0,(screen_width - enemy_width))

    character_x_pos += to_x * dt
    if character_x_pos <0 :
        character_x_pos=0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width

    
    ######### 4 collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect) :
        print("crash!")
        running = False

    ######### 5 put on the screen
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
   
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    #screen.blit(enemy2,(enemy_x_pos,enemy_y_pos))


    # timer
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000  # ms/1000 = per second

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
     # letter, True, font color 
    screen.blit(timer, (10,10))
    # time limit

    

    if total_time -elapsed_time <= 0 :
        print("time out")
        running = False

    pygame.display.update() #keep the img while roop 

#delay closing 
pygame.time.delay(2000) # 2 seconds delay

# close
pygame.quit()