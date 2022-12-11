import pygame
from Player import Player
from Ede import Ede

# La class qui permet de regrouper toute les classe et les rendre iterable entre elle
class Game:

    def __init__(self, background, screen):
        
        #Obligé de crée un groupe de joueur meme en solo 😭
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.all_ede = pygame.sprite.Group()
        self.ede = Ede(self)
        self.all_ede.add(self.ede)

        # Dictionnaire qui contient tout les boutons presser
        self.pressed = {}

        # Les variables a conserver pour actualiser la fenetre
        self.background = background
        self.screen = screen
    
    # Fonction qui actualise la fenetre ça permettra d'eviter de surchager main.py
    def refreshscreen(self):
        self.screen.blit(self.background, (0, -200))
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.ede.image, self.ede.rect)