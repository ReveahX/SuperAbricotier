import pygame
from Ede import Ede


#Le truc dans la parenthese c'est pour pouvoir avoir des sprites
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        
        #Je sais pas c'est quoi mais on a besoins pour que ça marche je sais que c'est en lien avec le truce en parametre de class
        super().__init__()
        #On en aurat besoins au moment des hitbox
        self.game = game

        #Charge les stats
        self.health = 100
        self.maxhealth = 100
        self.velocity = 10

        # Un dictionnaire qui contient tout type de munition et leur nombre pour les effets voir le README
        self.ammo = {"yellow": 0, "blue":0, "red":0, "green":0, "purple":0, "orange":0, "gold":0}
        self.maxammo = 1000 # Valeur a changer faut voire au moment de l'equillibrage
        self.damage_multiplier = 1
        self.attack = 10 

        self.coin = 0

        #Load le sprite
        self.image = pygame.image.load("Assets/Player.png")
        self.image = pygame.transform.scale(self.image, (240, 260))
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Coordonnée qui me semble pas mal
        self.rect.x = 400
        self.rect.y = 425
        self.start_y = self.rect.y

        self.isjump = False
        self.jumpcount = 11

        self.isjump = False


    
    #Les commande de mouvements seulement droite gauche pour le moment flemme de faire la gravité
    #Faut rajouter un check si on va a droite et a gauche en meme temps et ne rien faire
    def moveright(self):
        self.rect.x += self.velocity
        
        

    def moveleft(self):
        self.rect.x -= self.velocity
        
    def jump(self):
        # Boucle le temps du saut
        while self.isjump == True:
            pygame.display.flip()
            self.game.screen.blit(self.game.background, (0, -200))
            self.game.screen.blit(self.game.player.image, self.game.player.rect)

            # Bouge a droite si toujours dans la map
            if self.game.pressed.get(pygame.K_d) and self.rect.x + self.game.player.rect.width < self.game.screen.get_width():
                self.moveright()
                
            # Bouge a gauche si toujours dans la map
            elif self.game.pressed.get(pygame.K_q) and self.rect.x > 0:
                self.moveleft()

            # Monte jusqu'a etteindre la hauteur maximum
            if self.jumpcount >= -12:
                self.rect.y -= ((self.jumpcount) * abs(self.jumpcount)) * 0.5
                self.jumpcount -= 1

            #Descend jusqu'a atterrir
            else:
                self.jumpcount = 11
                self.isjump = False
                self.rect.y = self.start_y

            # Delay pour que ce ne soit pas instantanné
            pygame.time.delay(15)
