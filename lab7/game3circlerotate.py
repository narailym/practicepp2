import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("game")
icon = pygame.image.load("fonts/i.webp")
icon = pygame.transform.scale(icon, (500, 500))

clock = pygame.time.Clock()

running = True
x = 250
y = 250

up_limit = 25
down_limit = 475
right_limit = 475
left_limit = 25

while running:
    pygame.display.update()
    screen.blit(icon, (0, 0))

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pressed[pygame.K_UP] and y >= up_limit:
        y -= 20
        y = max(y, up_limit)
    if pressed[pygame.K_DOWN] and y <= down_limit:
        y += 20
        y = min(y, down_limit)
    if pressed[pygame.K_RIGHT] and x <= right_limit:
        x += 20
        x = min(x, right_limit)
    if pressed[pygame.K_LEFT] and x >= left_limit:
        x -= 20
        x = max(x, left_limit)

    pygame.draw.circle(screen, (9, 247, 242), (x, y), 35)
    pygame.display.flip()
    clock.tick(60)