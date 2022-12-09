import pygame
from Player import Player

class Game:

    def __init__(self):
        #Obligé de crée un groupe de joueur meme en solo 😭
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)