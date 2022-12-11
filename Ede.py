import pygame

# Le meilleur Compagnons
class Ede(pygame.sprite.Sprite):

    def __init__(self, game):
        
        #Le truc qui fait je sais pas quoi mais qui est nécessaire
        super().__init__()

        self.game = game
        self.velocity = 10

        #Le Sprite
        self.image = pygame.image.load("Assets/EdE.png")
        self.image = pygame.transform.scale(self.image, (120, 100) )
        self.image = pygame.transform.flip(self.image, 90, 0)
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Les coordonné
        self.rect.x = 0 #390
        self.rect.y = 450 #450

        #Les variable pour l'animation de vol
        self.flynb = 0
        self.isup = True

    #Commande pour suivre le joueur faudrat rajouter des mouvement random si Ede est dans balise
    def followplayer(self):
        balise = [self.game.player.rect.x - 400, self.game.player.rect.x + 400]
        if self.rect.x in balise:
            return
        elif self.rect.x < self.game.player.rect.x:
            self.image = pygame.transform.flip(self.image, 90, 0)
            self.rect.x += 3
        elif self.rect.x > self.game.player.rect.x:
            self.rect.x -= 3
        self.game.refreshscreen()

    
    # Fonction qui fait que Ede flotter dans les airs plutôt que d'être freeze
    def fly(self):

        if self.isup == True:
            self.rect.y -= 1
            self.flynb += 1
        else:
            self.rect.y += 1
            self.flynb += 1

        if self.flynb == 10:
            self.flynb = 0
            self.isup = not self.isup
        

