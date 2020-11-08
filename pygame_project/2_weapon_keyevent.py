# avoid flying poo
import pygame, random ,os 

pygame.init()

clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")

background =pygame.image.load(os.path.join(image_path,"background.png"))
stage =pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size= stage.get_rect().size # get size of img
stage_width = stage_size[0]
stage_height= stage_size[1]


character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size= character.get_rect().size # get size of img
character_width = character_size[0]
character_height= character_size[1]

character_x_pos = screen_width/2 - character_width/2 # on the half of the screen
character_y_pos = screen_height -character_height -stage_height #on the bottom of screen 

# spot  움직이기위해서 캐릭터 이동 방향 
to_x =0
to_y =0

#speed
character_speed = 0.6
#nemy_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size= weapon.get_rect().size # get size of img
weapon_width = weapon_size[0]
# 한번에 여러번 발사 가능
weapons= []
weapon_speed = 10




# Enemy
# enemy = pygame.image.load("C:/Users/YURI\Desktop/pythonworkspace/pygame_basic/enemy.jpg")
# enemy_size= enemy.get_rect().size # get size of img
# enemy_width = enemy_size[0]
# enemy_height= enemy_size[1]



# # for moving 
# enemy_x_pos = random.randint(0,(screen_width - enemy_width))  # on the half of the screen
# enemy_y_pos = 0 #(screen_height /2) - (enemy_height /2)


#enemy2.pygame.draw.rect(screen, (134,229,127), (enemy_x_pos,0,50,50), 2)

game_font = pygame.font.Font(None , 40) #default 
total_time = 100

# start time
start_ticks = pygame.time.get_ticks() # start


running = True
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
            elif event.key == pygame.K_SPACE: # weapon 스페이스 누르면
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos - character_height
                weapons.append([weapon_x_pos, weapon_y_pos])
        
    #     #when player don't push 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # enemy_y_pos += enemy_speed 
    # if enemy_y_pos > screen_height :
    #     enemy_y_pos = 0 
    #     enemy_x_pos = random.randint(0,(screen_width - enemy_width))

    character_x_pos += to_x * dt
    if character_x_pos <0 :
        character_x_pos=0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width- character_width

    # 무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed]  for w in weapons] # 무기 위치를 위로 쭉 올리는것
    # weapon이라는 리스트에서 하나의 무기 w를 가져오는데 이 w 웨폰도 리스트라서 
    # 그 리스트 안의 0번째 값과 1번째갚에서 웨폰스피드를 뺀 값을 다시 웨폰에 넣어주는 것 
    # x는 그대로고 y만 변경되고 있음 
    # 천장에 닿으면 없애기
    weapons = [ [w[0], w[1] ]  for w in weapons if w[1] > 0 ] #y좌표가 0보다 큰것만 

    # ######### 4 collision
    # character_rect = character.get_rect()
    # character_rect.left = character_x_pos
    # character_rect.top = character_y_pos

    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos

    # if character_rect.colliderect(enemy_rect) :
    #     print("crash!")
    #     running = False

    ######### 5 put on the screen
    screen.blit(background,(0,0))
    #weapon
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos) )

    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
   
    
    
    # screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    #screen.blit(enemy2,(enemy_x_pos,enemy_y_pos))


    # # timer
    # elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000  # ms/1000 = per second

    # timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    #  # letter, True, font color 
    # screen.blit(timer, (10,10))
    # # time limit

    

    # if total_time -elapsed_time <= 0 :
    #     print("time out")
    #     running = False

    pygame.display.update() #keep the img while roop 

#delay closing 
pygame.time.delay(2000) # 2 seconds delay

# close
pygame.quit()