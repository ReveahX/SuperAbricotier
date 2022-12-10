import pygame
from Player import Player
from Game import Game


# Crée la fenêtre
pygame.init()
pygame.display.set_caption("Drexa")
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

# Charge un fond d'écran
background = pygame.image.load('assets/bg.jpg')

# Charge le jeux
game = Game()

isjump = False
Running = True

# Pour que le jeu continue
while Running:
    clock.tick
    # Actualise l'ecran en boucle (pour pas avoir d'image figer)
    pygame.display.flip()

    # Dessine sur l'écran le background et le joueur
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)
    #screen.blit(game.ede.image, game.ede.rect)

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
            # Commence a enregistrer le temps de pressions de la touche espace
            if event.key == pygame.K_SPACE and not game.player.isjump:
                sp_start = pygame.time.get_ticks()

        # ... et la lache
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
            # Calcule la hauteur de saut a eteindre 
            if event.key == pygame.K_SPACE and not game.player.isjump:
                sp_time = pygame.time.get_ticks() - sp_start + 380
                
                game.player.maxjump = min(12, sp_time // 40)
                game.player.jumpcount = game.player.maxjump
                game.player.isjump = True

    
    # Fait un saut 
    if game.player.isjump:
        # Prend de la hauteur jusqu' a ce que le joueur ateigne sa hauteur max
        if game.player.jumpcount >= -game.player.maxjump:
            game.player.rect.y -= (game.player.jumpcount * abs(game.player.jumpcount)) * 0.5
            game.player.jumpcount -= 1
        # Descend jusqu'a arriver au coordonner de départ
        else:
            game.player.jumpcount = game.player.maxjump
            game.player.isjump = False
            temp = game.player.start_y - game.player.rect.y
            game.player.rect.y = game.player.start_y
        pygame.time.delay(15)
            

# Pour faire culpabiliser le joueur quand il quitte le jeux 
# (en vrai c'etait juste un truc de debug a la creation de la fenetre)
print("Tu pars déja 😢")