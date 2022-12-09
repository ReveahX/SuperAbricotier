import pygame

pygame.init()

pygame.display.set_caption("Drexa")
screen = pygame.display.set_mode((1080, 720))


#background = pygame.image.load('assets/bg.png')


Running = True

while Running:
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()

print("Tu pars déja 😢")