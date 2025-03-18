import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Play")

icon = pygame.image.load("fonts/white2.png")
icon = pygame.transform.scale(icon, (600, 600))

music = [ "sound/Akmaralym.mp3", "sound/Into it.mp3", "sound/What_Goes_Around_Comes_Around.mp3"
]

stop =  pygame.image.load("images/stop.png")
stop = pygame.transform.scale(stop, (150, 150))
play = pygame.image.load("images/play.png")
play = pygame.transform.scale(play, (150, 150))
toleft = pygame.image.load("images/left.png")
toleft = pygame.transform.scale(toleft, (150, 150))
toright = pygame.image.load("images/right.png")
toright = pygame.transform.scale(toright, (150, 150))

image1 = pygame.image.load("fonts/мейрамбек.webp")
image1 = pygame.transform.scale(image1, (450, 300))

image2 = pygame.image.load("fonts/chase.webp")
image2 = pygame.transform.scale(image2, (450, 300))

image3 = pygame.image.load("fonts/justin.jpg ")
image3 = pygame.transform.scale(image3, (450, 300))

clock = pygame.time.Clock()

running = True
stop_play = [play, stop]
counter = 0


image = [image1, image2, image3]
current_song = 0

pygame.mixer.music.load(music[current_song])
pygame.mixer.music.play()

while running:
    pygame.display.update()
    screen.blit(icon, (0, 0))
    screen.blit(image[current_song], (75, 50))
    screen.blit(stop_play[counter], (225, 400))
    screen.blit(toright, (425, 400))
    screen.blit(toleft, (25, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    counter = (counter + 1) % len(stop_play)

                else:
                    pygame.mixer.music.unpause()
                    counter = (counter - 1) % len(stop_play)




            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(music)
                pygame.mixer.music.load(music[current_song])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(music)
                pygame.mixer.music.load(music[current_song])
                pygame.mixer.music.play()

    clock.tick(60)

pygame.quit()