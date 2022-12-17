import pygame
from pygame.locals import *

class Lumberjack(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()

        self.game = game


        self.health = 10
        self.maxhealth =10

        self.velocity = 7
        self.velocity_limits = [-3, 3]

        self.attack = 10

        self.image = pygame.image.load("Assets/Lumberjack.png")
        self.image_right = self.image

        self.image = pygame.transform.flip(self.image, 90, 0)
        self.image_left = self.image
        self.image.get_rect()
        self.rect = self.image.get_rect()


        self.rect.x = 720
        self.rect.y = 500
    

    
    def move_towards_player(self):
        balise = [self.game.player.rect.x - 100, self.game.player.rect.x + 230]
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
        #self.game.refreshscreen()
        

    # Same thing using only pygame utilities
    def move_towards_player2(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      )
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.velocity)
        self.rect.move_ip(dirvect)