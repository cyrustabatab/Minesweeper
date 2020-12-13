import pygame,os



class Tile(pygame.sprite.Sprite):

    image = pygame.image.load(os.path.join('assets','block.png'))

    def __init__(self,x,y,tile_size=16):
        super().__init__()
        self.x = x
        self.y = y
        if tile_size != 16:
            self.image = pygame.transform.scale(self.image,(tile_size,tile_size))

        self.rect = self.image.get_rect(topleft=(self.x,self.y))















