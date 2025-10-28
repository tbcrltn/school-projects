import pygame


screen = pygame.display.set_mode((1200, 600))
x = 50
y = 500
speed = 6
y_vel = 0
x_vel = 0
jump_timer = 100
level = 1



def game_logic(x, y, y_vel, player, ground, jump_timer, speed, x_vel, flag, level):
    #check movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x_vel = speed
    if keys[pygame.K_LEFT]:
        x_vel = -speed

    if keys[pygame.K_UP] and jump_timer > 50:
        for platform in ground:
            if player.colliderect(platform):
                y_vel = -10  
                jump_timer = 0

    #velocity handling
    y_vel += 0.5
    y += y_vel
    if x_vel < 0:
        x_vel += 0.5
    elif x_vel > 0:
        x_vel -= 0.5

    x += x_vel

    #check for collision with ground
    for platform in ground:

        if player.colliderect(platform):
            if y_vel > 0 and player.bottom <= platform.top + y_vel:
                player.bottom = platform.top
                y = player.top
                y_vel = 0
                jump_timer = 100

    #check if player reached goal

    if player.colliderect(flag):
        level += 1
        x, y, y_vel, x_vel, jump_timer = reset()

    return x, y, y_vel, jump_timer, x_vel, level

def reset():
    x = 50
    y = 500
    y_vel = 0
    x_vel = 0
    jump_timer = 100
    return x, y, y_vel, x_vel, jump_timer





running = True
while running:
    #check for screen close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #change screen color to black
    screen.fill((0, 0, 0))

    #draw player
    player = pygame.draw.rect(screen, (0, 0, 255), (x, y, 20, 20))

    #draw levels
    if level == 1:
        ground = [pygame.draw.rect(screen, (0, 0, 255), (0, 550, 1200, 100)),
                pygame.draw.rect(screen, (0, 0, 255), (400, 500, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (300, 425, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (200, 350, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (400, 275, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (600, 275, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (800, 275, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (1000, 200, 50, 10)),
                pygame.draw.rect(screen, (0, 0, 255), (600, 125, 250, 10))]
        flag = pygame.draw.rect(screen, (0, 100, 0), (610, 95, 20, 20))

    elif level == 2:
        ground = [pygame.draw.rect(screen, (0, 0, 255), (0, 550, 1200, 100)),
                  pygame.draw.rect(screen, (0, 0, 255), (100, 500, 50, 10)),
                  pygame.draw.rect(screen, (0, 0, 255), (150, 450, 40, 10)),
                  pygame.draw.rect(screen, (0, 0, 255), (200, 400, 30, 10)),
                  pygame.draw.rect(screen, (0, 0, 255), (250, 350, 20, 10)),
                  pygame.draw.rect(screen, (0, 0, 255), (300, 300, 10, 10))]
        flag = pygame.draw.rect(screen, (0, 100, 0), (470, 300, 20, 20))

    #call game logic
    x, y, y_vel, jump_timer, x_vel, level = game_logic(x, y, y_vel, player, ground, jump_timer, speed, x_vel, flag, level)
    

    #handle frame rate
    pygame.Clock().tick(60)
    pygame.display.update()