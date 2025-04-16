import pygame
import random
import sys
import psycopg2

pygame.init()

screenwidth = 600
screenh= 400
sizeofgrid = 20
widthgrid = screenwidth // sizeofgrid
hgrid = screenh // sizeofgrid
screen = pygame.display.set_mode((screenwidth, screenh))
pygame.display.set_caption("SNAKE")

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="acerAN"
)

white = (255, 255, 255)
black = (0, 0, 0)
bluish = (66, 135, 245)

class Snake:
    def __init__(self):
        self.body = [(widthgrid // 2, hgrid // 2)]
        self.direction = (1, 0)
        self.player_name = None
        self.user_id = None
        self.paused = False

    def get_player_name(self):
        input_box = pygame.Rect(screenwidth // 2 - 100, screenh // 2 - 25, 200, 50)
        font = pygame.font.Font(None, 32)
        color_inactive = pygame.Color(255, 0, 0)
        color_active = pygame.Color(0, 255, 0)
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            screen.fill(black)
            txt_surface = font.render(text, True, color)
            input_box.w = max(200, txt_surface.get_width() + 10)
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()

        self.player_name = text

    def move(self):
        global score, speed, level
        if not self.paused:
            head = self.body[0]
            x = (head[0] + self.direction[0]) % widthgrid
            y = (head[1] + self.direction[1]) % hgrid
            new_head = (x, y)
            if new_head in self.body[1:] or new_head in walls:
                return False
            self.body.insert(0, new_head)
            if new_head == food.position:
                score += 1
                if score % 5 == 0:
                    level += 1
                    speed, walls[:] = load_level(level)
                food.spawn()
            else:
                self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.weight = 20
        self.color = bluish
        self.timer = 0
        self.spawn()

    def spawn(self):
        while True:
            x = random.randint(0, widthgrid - 1)
            y = random.randint(0, hgrid - 1)
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                self.weight = random.choice([10, 20, 30, 40])
                self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 105, 180)])
                self.timer = pygame.time.get_ticks() + 4000
                break

    def update(self):
        if pygame.time.get_ticks() - self.timer > 0:
            self.spawn()

def create_user(username):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                cur.execute("INSERT INTO users(username) VALUES (%s) RETURNING id;", (username,))
                user_id = cur.fetchone()[0]
                conn.commit()
                return user_id
    except Exception as error:
        print("Ошибка create_user:", error)
        conn.rollback()
        return None

def loadlastscore(username):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT us.score, us.level
                FROM user_score us
                JOIN users u ON us.user_id = u.id
                WHERE u.username = %s
                ORDER BY us.played_at DESC
                LIMIT 1;
            """, (username,))
            result = cur.fetchone()
            return result if result else (0, 0)
    except Exception as error:
        print("Ошибка при загрузке результата:", error)
        conn.rollback()
        return (0, 0)

def insert_user_score(user_id, score, level):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s);
            """, (user_id, score, level))
            conn.commit()
    except Exception as error:
        print("Ошибка при сохранении результата:", error)
        conn.rollback()

def load_level(level):
    speed = 10 + level
    walls = []
    if level == 1:
        walls += [(i, 10) for i in range(5, 25)]
    elif level == 2:
        walls += [(i, 5) for i in range(10, 20)] + [(i, 15) for i in range(10, 20)]
    elif level >= 3:
        walls += [(10, i) for i in range(5, 15)] + [(20, i) for i in range(5, 15)]
    walls += [(0, i) for i in range(hgrid)]
    walls += [(widthgrid - 1, i) for i in range(hgrid)]
    walls += [(i, 0) for i in range(widthgrid)]
    walls += [(i, hgrid - 1) for i in range(widthgrid)]
    return speed, walls

snake = Snake()
snake.get_player_name()
snake.user_id = create_user(snake.player_name)
score, level = loadlastscore(snake.player_name)
speed, walls = load_level(level)
food = Food()
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            elif event.key == pygame.K_SPACE:
                snake.paused = not snake.paused
                if snake.paused and snake.user_id:
                    insert_user_score(snake.user_id, score, level)
            elif event.key == pygame.K_ESCAPE:
                running = False

    if not snake.move():
        running = False

    if not snake.paused:
        for segment in snake.body:
            pygame.draw.rect(screen, white, (segment[0] * sizeofgrid, segment[1] * sizeofgrid, sizeofgrid, sizeofgrid))

        x, y = food.position
        pygame.draw.rect(screen, food.color, (x * sizeofgrid, y * sizeofgrid, food.weight, food.weight))

        for wall in walls:
            pygame.draw.rect(screen, (100, 100, 100), (wall[0] * sizeofgrid, wall[1] * sizeofgrid, sizeofgrid, sizeofgrid))

    font = pygame.font.SysFont(None, 25)
    text = font.render(f"score: {score}   level: {level}", True, white)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    food.update()
    clock.tick(speed)

if snake.user_id:
    insert_user_score(snake.user_id, score, level)
pygame.quit()
conn.close()
