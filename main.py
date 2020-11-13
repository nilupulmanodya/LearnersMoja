import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos+600, 450))

def create_drop():
    new_drop = drop_surface.get_rect(center =(800,550))
    return  new_drop

def move_drop(drops):
    for drop in drops:
        drop.centerx -=5
    return drops

def draw_drops(drops):
    for drop in drops:
        screen.blit(drop_surface,drop)


#game variables

gravity = 0.15
bike_movement = 0

pygame.init()
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("Assets/background.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("Assets/floor.png").convert()
floor_x_pos = 0

bike_surface = pygame.image.load("Assets/bike horizontal.png").convert_alpha()
bike_rect = bike_surface.get_rect(center=(180,450))

lorry_surface = pygame.image.load("Assets/lastlorry.png").convert_alpha()
lorry_rect = lorry_surface.get_rect(center = (1000,450))

drop_surface = pygame.image.load("Assets/drop.png").convert_alpha()
drop_list = []
SPAWNDROP = pygame.USEREVENT
pygame.time.set_timer(SPAWNDROP,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bike_movement=-8
                bike_rect.centery += bike_movement

        if event.type == SPAWNDROP:
            drop_list.append(create_drop())



    screen.blit(bg_surface,(0,-300))


    #floor
    floor_x_pos -=1.5
    draw_floor()
    if floor_x_pos <= -145:
        floor_x_pos =0


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

    screen.blit(bike_surface, bike_rect)
    screen.blit(lorry_surface,lorry_rect)

    pygame.display.update()
    clock.tick(120)