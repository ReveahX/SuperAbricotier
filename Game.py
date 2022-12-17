import pygame
from Player import Player
from Ede import Ede
from Lumberjack import Lumberjack

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

        self.all_lumberjack = pygame.sprite.Group()
        self.Lumberjack = Lumberjack(self)
        self.all_lumberjack.add(self.Lumberjack)

        # Dictionnaire qui contient tout les boutons presser
        self.pressed = {}

        # Les variables a conserver pour actualiser la fenetre
        self.background = background
        self.screen = screen

        self.Running = True
    
    # Fonction qui actualise la fenetre ça permettra d'eviter de surchager main.py
    def refreshscreen(self):
        self.screen.blit(self.background, (0, -200))
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.ede.image, self.ede.rect)
        self.screen.blit(self.Lumberjack.image, self.Lumberjack.rect)
        pygame.display.flip()
    
    def mainmenu(self):
        on_menu = True
        self.isjuststart = True
        while on_menu:
            backgroundcolor = (0, 0, 0)
            self.screen.fill(backgroundcolor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on_menu = False
                    self.Running = False, False
                    pygame.quit
                if event.type == pygame.KEYUP:
                    self.pressed[event.key] = True
                if self.pressed.get(pygame.K_ESCAPE):
                    for i in self.pressed:
                        self.pressed[i] = False
                    on_menu = False
                    self.isjuststart = False
                    self.pressed = {} 