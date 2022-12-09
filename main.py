import pygame
from Player import Player
from Game import Game


# Crée la fenêtre
pygame.init()
pygame.display.set_caption("Drexa")
screen = pygame.display.set_mode((1080, 720))

# Charge un fond d'écran
background = pygame.image.load('assets/bg.jpg')

# Charge le jeux
game = Game()


Running = True

# Pour que le jeux continue
while Running:
    # Actualise l'ecran en boucle (pour pas avoir d'image figer)
    pygame.display.flip()

    # Dessine sur l'écran le background et le joueur
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    # Bouge a droite si toujours dans la map
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveright()

    # Bouge a gauche si toujours dans la map
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.moveleft()

    for event in pygame.event.get():

        # Check si le joueur a quitter (sa permet d'eviter un crash mais faut pas le dire)
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()

        # Check si le joueur appuis sur une touche...
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        # ... et la lache
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

# Pour faire culpabiliser le joueur quand il quite le jeux 
# (en vrai c'etait juste un truc de debug a la creation de la fenetre)
print("Tu pars déja 😢")