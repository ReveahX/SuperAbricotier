import pygame
from Player import Player
from Ede import Ede

class Game:

    def __init__(self, background, screen):
        
        #Obligé de crée un groupe de joueur meme en solo 😭
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.all_ede = pygame.sprite.Group()
        self.ede = Ede(self)
        self.all_ede.add(self.ede)

        #Dictionnaire qui contient tout les boutons utiliser
        self.pressed = {}

        self.background = background
        self.screen = screen