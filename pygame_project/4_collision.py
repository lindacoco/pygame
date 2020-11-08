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

# balls
ball_images = [
    pygame.image.load(os.path.join(image_path,"ball1.png")),
    pygame.image.load(os.path.join(image_path,"ball2.png")),
    pygame.image.load(os.path.join(image_path,"ball3.png")),
    pygame.image.load(os.path.join(image_path,"ball4.png"))
]

# 큰공은 크게 튄다 공크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9 ] #올라갈때는 y값이 - 되니까

# 공들
balls = []

balls.append({
    "pos_x" : 50, #공의 x 좌표
    "pos_y" : 50,
    "img_idx": 0, #공의 이미지 인덱스
    "to_x": 3 , #공의 x축 이동 방향 -이면 왼쪽 
    "to_y" : -6,
    "init_spd_y" :ball_speed_y[0] #y최초속도

})


#사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


# msg
msg = pygame.image.load(os.path.join(image_path,"gg.png"))

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
    
    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1] ]  for w in weapons if w[1] > 0 ] #y좌표가 0보다 큰것만 
    
    #공 위치 정의
    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로 벽에 닿았을 때 공 이동 위치 변경 튕겨나오는 효과
        if ball_pos_x <0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height :
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 속도를 줄여나감 .. 포물선
            ball_val["to_y"] += 0.5 

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



    # ######### 4 collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect() # 공 rect정보 업데이트
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 1 공과 캐릭터 충돌 
        if character_rect.colliderect(ball_rect):
            #screen.blit(msg,(150,200))
            running = False
            break

        # 2 공과 무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect): #변수 선언해주고
                weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_index  # 해당 공 없애기 위한 값 설정 
                break
         
    # 충돌된 공 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1    



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

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y ))

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