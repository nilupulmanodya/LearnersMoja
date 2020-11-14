import pygame, sys
import time

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos+600, 450))

def create_drop():
    new_drop = drop_surface.get_rect(center =(800,520))
    return  new_drop

def move_drop(drops):
    for drop in drops:
        drop.centerx -=8
    return drops

def draw_drops(drops):
    for drop in drops:
        screen.blit(drop_surface,drop)

def check_collision(drops):
    for drop in drops:
        if bike_rect.colliderect(drop):
            return False

        if bike_rect.top <0 :
            return False
    return True

def rotate_bike(bike):
    new_bike = pygame.transform.rotozoom(bike,-bike_movement,1)
    return new_bike

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(f'Score : {str(int(score))}',True,(2, 30, 75))
        score_rect = score_surface.get_rect(center=(600,60))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score : {str(int(score))}', True, (2, 30, 75))
        score_rect = score_surface.get_rect(center=(600, 60))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score : {str(int(highscore))}', True, (12, 167, 151))
        high_score_rect = high_score_surface.get_rect(center=(600, 555))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score,highscore):
    if score>highscore:
        highscore = score
    return highscore

def open_game():
    time.sleep(1)




#game variables

gravity = 0.2
bike_movement = 0
game_active =True
score = 0
highscore = 0

pygame.init()

game_font = pygame.font.Font('freesansbold.ttf',60)
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()


bg_surface = pygame.image.load("Assets/background.png").convert_alpha()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("Assets/floor.png").convert_alpha()
floor_x_pos = 0

bike_surface = pygame.image.load("Assets/bike.png").convert_alpha()
bike_rect = bike_surface.get_rect(center=(180,450))

lorry_surface = pygame.image.load("Assets/lorry.png").convert_alpha()
lorry_rect = lorry_surface.get_rect(center = (1000,450))

gameover_surface = pygame.image.load("Assets/over restart.png").convert_alpha()
gameover_rect = gameover_surface.get_rect(center=(600,260))

drop_surface = pygame.image.load("Assets/drop.png").convert_alpha()
drop_list = []
SPAWNDROP = pygame.USEREVENT
pygame.time.set_timer(SPAWNDROP,1200)

open_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and game_active :
            if event.key == pygame.K_SPACE:
                bike_movement=-8
                bike_rect.centery += bike_movement

        if event.type == SPAWNDROP:
            drop_list.append(create_drop())

        if event.type == pygame.KEYDOWN and game_active == False:
            drop_list.clear()
            game_active =True
            bike_rect.center=(180,450)
            bike_movement = 0
            score = 0



    screen.blit(bg_surface,(0,-300))


    #floor
    floor_x_pos -=1.5
    draw_floor()
    if floor_x_pos <= -145:
        floor_x_pos =0

    if game_active:
        score +=0.01
        game_active = check_collision(drop_list)
        #drops
        drop_list = move_drop(drop_list)
        draw_drops(drop_list)


        #bike

        if bike_rect.centery <= 450:
            bike_movement += gravity
            bike_rect.centery+=bike_movement


        else :
            bike_movement = 0
            bike_rect.centery = 450
        rotated_bike = rotate_bike(bike_surface)
        screen.blit(rotated_bike, bike_rect)
        screen.blit(lorry_surface,lorry_rect)

        score_display('main_game')

    else:
        highscore = update_score(score,highscore)
        score_display('game_over')
        screen.blit(gameover_surface,gameover_rect)
    pygame.display.update()
    clock.tick(120)