import pygame

screen = pygame.display.set_mode((600, 600))
image_source = pygame.image.load("C:/Users/tbcrl/Documents/school-projects/ImageProcessing/bears_copy.jpg")
image_source = pygame.transform.scale(image_source, (200, 100))
image = pygame.Rect(250,200,200,100)
right = True
speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(image_source, image)
    if right:
        image.x += speed
    else:
        image.x -= speed

    if image.x <= 0:
        right = True

    elif image.x >= 400:
        right = False

    

    pygame.display.update()
    pygame.Clock().tick(60)