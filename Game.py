import pygame
from Player import Player
from Ede import Ede

class Game:

    def __init__(self):
        
        #Obligé de crée un groupe de joueur meme en solo 😭
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.all_ede = pygame.sprite.Group()
        self.ede = Ede(self)

        #Dictionnaire qui contient tout les boutons utiliser
        self.pressed = {}