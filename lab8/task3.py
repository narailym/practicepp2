import sys
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Program")


tool = "line"  
color = BLACK 
draw = False  
shapes = []  
start_pos = None  


def draw_shape(surface, shape):

    tool, color, start, end = shape
    if tool == "line":
        pygame.draw.line(surface, color, start, end, 3)
    elif tool == "square":
        rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
        pygame.draw.rect(surface, color, rect, 3)
    elif tool == "circle":
        radius = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        pygame.draw.circle(surface, color, start, radius, 3)


def main():
    
    global tool, color, draw, start_pos

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    tool = "line"
                elif event.key == pygame.K_s:
                    tool = "square"
                elif event.key == pygame.K_c:
                    tool = "circle"
                elif event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_d:
                    shapes.clear() 
                elif event.key == pygame.K_q:
                    shapes.clear() 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    draw = True
                    start_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    draw = False
                    end_pos = event.pos
                    shapes.append((tool, color, start_pos, end_pos)) 

        for shape in shapes:
            draw_shape(screen, shape)

        if draw:
            end_pos = pygame.mouse.get_pos()
            draw_shape(screen, (tool, color, start_pos, end_pos))

        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
