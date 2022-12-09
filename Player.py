import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self):
        
        #Je sais pas c'est quoi mais on a besoins pour que ça marche
        super().__init__()

        #Load les stats
        self.health = 100
        self.maxhealth = 100
        self.attack = 10
        self.velocity = 1

        #Load le sprite
        self.image = pygame.image.load("Assets/player.png")
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Coordonnée a changer plus tard
        self.rect.x = 0
        self.rect.y
    
    #Les commande de mouvements seulement droite gauche pour le moment flemme de faire la gravité
    def moveright(self):
        self.rect.x += self.velocity

    def moveleft(self):
        self.rect.x -= self.velocity