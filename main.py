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

game.mainmenu()
# Pour que le jeu continue
while game.Running:
    
    
        

    game.Lumberjack.move_towards_player()


    game.player.jump()
    #print(game.player.rect.x)
    #print(game.ede.rect.x)
    game.ede.followplayer()

    pygame.time.delay(14)
    clock.tick
    game.ede.fly()

    game.ede.followplayer()

    
    

    # Dessine sur l'écran le background et le joueur et actualise l'écran
    game.refreshscreen()
    
    if game.pressed.get(pygame.K_SPACE):
        game.player.isjump = True
        game.player.jump()

    # Bouge a droite si toujours dans la map
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width() and not game.pressed.get(pygame.K_q):
        game.player.moveright()
        #pygame.time.delay(15)

    # Bouge a gauche si toujours dans la map
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0 and not game.pressed.get(pygame.K_d):
        game.player.moveleft()
        #pygame.time.delay(15)


    for event in pygame.event.get():

        # Check si le joueur a quitter (sa permet d'eviter un crash mais faut pas le dire)
        if event.type == pygame.QUIT:
            game.Running = False
            pygame.quit()

        # Check si le joueur appuis sur une touche...
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        # ... et la lache
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False


# Pour faire culpabiliser le joueur quand il quitte le jeux 
# (en vrai c'etait juste un truc de debug a la creation de la fenetre)
print("Tu pars déja 😢")