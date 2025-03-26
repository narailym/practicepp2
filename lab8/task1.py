import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Racer game")

road = pygame.image.load("images/Street.png")
road = pygame.transform.scale(road, (500, 400))

car = pygame.image.load("images/Player.png")
car = pygame.transform.scale(car, (100, 100))

coin = pygame.image.load("images/coin.png")
coin = pygame.transform.scale(coin, (30, 30))

enemy = pygame.image.load("images/Enemy.png")
enemy = pygame.transform.scale(enemy, (100, 100))

clock = pygame.time.Clock()
road_y = 0
speed = 5

left_limit = 60
right_limit = 460
x = 260
y = 200

money_size = 30
car_size = 100
MoneyList = []
CarList = []

last_coin_time = time.time()
coin_delay = 3

last_coin_time1 = time.time()
enemy_delay = 3

money_speed = 3
car_speed = 3
score = 0

running = True
font = pygame.font.Font(None, 36)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x >= left_limit:
                x -= 200
                x = max(x, left_limit)
            elif event.key == pygame.K_RIGHT and x <= right_limit:
                x += 200
                x = min(x, right_limit)

    if time.time() - last_coin_time > coin_delay:
        money_x = random.choice([100, 300, 500])
        MoneyList.append([money_x, -money_size])
        last_coin_time = time.time()

    for money in MoneyList:
        money[1] += money_speed

    car_rect = pygame.Rect(x, y, 100, 100)
    for money in MoneyList[:]:
        money_rect = pygame.Rect(money[0], money[1], money_size, money_size)
        if car_rect.colliderect(money_rect):
            MoneyList.remove(money)
            score += 1
    MoneyList = [money for money in MoneyList if money[1] < 460]

    if time.time() - last_coin_time1 > enemy_delay:
        car_x = random.choice([100, 250, 400])
        CarList.append([car_x, -car_size])
        last_coin_time1 = time.time()

    for enemy_car in CarList:
        enemy_car[1] += car_speed

    car_rect = pygame.Rect(x, y, 100, 100)
    for enemy_car in CarList[:]:
        enemycar_rect = pygame.Rect(enemy_car[0], enemy_car[1], car_size, car_size)
        if car_rect.colliderect(enemycar_rect):
            running = False

    CarList = [car for car in CarList if car[1] < 460]

    road_y += speed
    if road_y >= 400:
        road_y = 0

    score_text = font.render(f"Score:{score} ", True, (255, 255, 255))

    screen.blit(road, (0, road_y - 400))
    screen.blit(road, (0, road_y))
    screen.blit(car, (x, y))
    screen.blit(score_text, (10, 10))

    for money in MoneyList:
        screen.blit(coin, (money[0], money[1]))

    for enemy_car in CarList:
        screen.blit(enemy, (enemy_car[0], enemy_car[1]))

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
