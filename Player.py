import pygame

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
        self.velocity = 3

        # Un dictionnaire qui contient tout type de munition et leur nombre pour les effets voir le README
        self.ammo = {"yellow": 0, "blue":0, "red":0, "green":0, "purple":0, "orange":0, "gold":0}
        self.maxammo = 1000 # Valeur a changer faut voire au moment de l'equillibrage
        self.damage_multiplier = 1
        self.attack = 10 

        self.coin = 0

        #Load le sprite
        self.image = pygame.image.load("Assets/Player.png")
        self.image.get_rect()
        self.rect = self.image.get_rect()

        #Coordonnée qui me semble pas mal
        self.rect.x = 400
        self.rect.y = 460

    
    #Les commande de mouvements seulement droite gauche pour le moment flemme de faire la gravité
    #Faut rajouter un check si on va a droite et a gauche en meme temps et ne rien faire
    def moveright(self):
        self.rect.x += self.velocity

    def moveleft(self):
        self.rect.x -= self.velocity