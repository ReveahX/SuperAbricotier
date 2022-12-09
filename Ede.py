import pygame

# Le meilleur Compagnons
class Ede(pygame.sprite.Sprite):

    def __init__(self, game):
        
        #Le truc qui fait je sais pas quoi mais qui est nécessaire
        super().__init__()

        self.game = game
        self.velocity = 3.2

        #Le Sprite
        self.image = pygame.image.load("Assets/Ed-e.gif")
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Les coordonné
        self.rect.x = 390
        self.rect.y = 450