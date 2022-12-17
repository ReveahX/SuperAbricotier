import pygame

# Le meilleur Compagnons
class Ede(pygame.sprite.Sprite):

    def __init__(self, game):
        
        #Le truc qui fait je sais pas quoi mais qui est nécessaire
        super().__init__()

        self.game = game
        self.velocity = 3
        self.velocity_limits = [-3, 3]

        #Le Sprite
        self.image = pygame.image.load("Assets/EdE.png")
        self.image = pygame.transform.scale(self.image, (120, 100) )
        self.image_left = self.image
        
        self.image = pygame.transform.flip(self.image, 90, 0)
        self.image_right = self.image
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Les coordonné
        self.rect.x = 0 #390
        self.rect.y = 430 #450

        #Les variable pour l'animation de vol
        self.flynb = 0
        self.isup = True
 #       self.flyspeed = 0.01

    #Commande pour suivre le joueur faudrat rajouter des mouvement random si Ede est dans balise
    def followplayer(self):
        balise = [self.game.player.rect.x - 80, self.game.player.rect.x + 200]
        if self.rect.x > balise[0] and self.rect.x < balise[1]:
            return
        
        if self.velocity < self.velocity_limits[0]:
            self.velocity = self.velocity_limits[0]
        elif self.velocity > self.velocity_limits[1]:
            self.velocity = self.velocity_limits[1]

        self.image = self.image_left if self.velocity < 0 else self.image_right

        self.rect.x += self.velocity

        if self.rect.x < balise[0]:
            self.velocity += 1
        elif self.rect.x > balise[1]:
            #self.image = pygame.transform.flip(self.image, 90, 0)
            self.velocity -= 1
        self.game.refreshscreen()


    # Fonction qui fait que Ede flotte dans les airs plutôt que d'être freeze
    def fly(self):
        #self.flyspeed = 1
        
        if self.isup == True:
            self.rect.y -= 1
            self.flynb += 1
        else:
            self.rect.y += 1
            self.flynb += 1

        if self.flynb == 10:
            self.flynb = 0
            self.isup = not self.isup

# A garder pour la fin du devellopement
#        if self.flynb < 2 or self.flynb > 8:
#            self.flyspeed = 1
#        else:
#            self.flyspeed = 2
        

