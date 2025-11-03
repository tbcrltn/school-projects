import pygame

screen = pygame.display.set_mode((600, 600))
image = pygame.image.load("C:/Users/tbcrl/Documents/school-projects/ImageProcessing/bears_copy.jpg")
image = pygame.transform.scale(image, (200, 100))
image_x = 250
image_y = 200
right = True
speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(image, (image_x, image_y))
    if right:
        image_x += speed
    else:
        image_x -= speed

    if image_x <= 0:
        right = True

    elif image_x >= 400:
        right = False

    

    pygame.display.update()
    pygame.Clock().tick(60)