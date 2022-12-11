import pygame
from Player import Player
from Game import Game


# Crée la fenêtre
pygame.init()
pygame.display.set_caption("Drexa")
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
logo = pygame.image.load("Assets/Logo.png")
pygame.display.set_icon(logo)

# Charge un fond d'écran
background = pygame.image.load('assets/bg.jpg')

# Charge le jeux
game = Game(background, screen)

isjump = False
Running = True


# Pour que le jeu continue
while Running:
    clock.tick
    # Actualise l'ecran en boucle (pour pas avoir d'image figer)
    pygame.display.flip()

    # Dessine sur l'écran le background et le joueur
    game.screen.blit(background, (0, -200))
    game.screen.blit(game.player.image, game.player.rect)
    #screen.blit(game.ede.image, game.ede.rect)

    
    if game.pressed.get(pygame.K_SPACE):
        game.player.isjump = True
        game.player.jump()

    # Bouge a droite si toujours dans la map
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width() and not game.pressed.get(pygame.K_q):
        game.player.moveright()
        pygame.time.delay(15)

    # Bouge a gauche si toujours dans la map
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0 and not game.pressed.get(pygame.K_d):
        game.player.moveleft()
        pygame.time.delay(15)


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


    if isjump:
        if game.player.jumpcount >= -10:
            game.player.rect.y -= ((game.player.jumpcount) * abs(game.player.jumpcount)) * 0.5
            game.player.jumpcount -= 1

            # Bouge a droite si toujours dans la map
            if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
                game.player.moveright()
            
            # Bouge a gauche si toujours dans la map
            elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
                game.player.moveleft()


        else:
            game.player.jumpcount = 10
            isjump = False
            temp = game.player.start_y - game.player.rect.y
            game.player.rect.y = game.player.start_y
        pygame.time.delay(15)

            

# Pour faire culpabiliser le joueur quand il quitte le jeux 
# (en vrai c'etait juste un truc de debug a la creation de la fenetre)
print("Tu pars déja 😢")