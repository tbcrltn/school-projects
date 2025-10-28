import pygame


screen = pygame.display.set_mode((600, 600))
x = 300
y = 300
speed = 5
y_vel = 0
jump_timer = 100



def check_movement(x, y, y_vel, player, ground, jump_timer, speed):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_UP] and jump_timer > 50:
        for platform in ground:
            if player.colliderect(platform):
                y_vel = -10  
                jump_timer = 0

    y_vel += 0.5
    y += y_vel

    for platform in ground:

        if player.colliderect(platform):
            if y_vel > 0 and player.bottom <= platform.top + y_vel:
                player.bottom = platform.top
                y = player.top
                y_vel = 0
                jump_timer = 100

    return x, y, y_vel, jump_timer




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player = pygame.draw.rect(screen, (0, 0, 255), (x, y, 20, 20))
    ground = [pygame.draw.rect(screen, (0, 0, 255), (0, 550, 600, 600)),
              pygame.draw.rect(screen, (0, 0, 255), (400, 500, 100, 10))]
    x, y, y_vel, jump_timer = check_movement(x, y, y_vel, player, ground, jump_timer, speed)
    
    pygame.Clock().tick(60)
    pygame.display.update()