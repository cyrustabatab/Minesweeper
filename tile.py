import pygame,os





class Tile(pygame.sprite.Sprite):

    block_image = pygame.image.load(os.path.join('assets','block.png'))
    mine_image = pygame.image.load(os.path.join('assets','mine.png'))
    empty_image = pygame.image.load(os.path.join('assets','empty.png'))


    def __init__(self,x,y,tile_size=16):
        super().__init__()
        self.x = x
        self.y = y
        self.tile_size = tile_size
        self.hidden_image = self.empty_image
        if tile_size != 16:
            self.image = pygame.transform.scale(self.block_image,(tile_size,tile_size))
            self.hidden_image = pygame.transform.scale(self.hidden_image,(tile_size,tile_size))
            

        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.is_mine = False
        self.clicked = False


    def mark_mine(self):
        self.is_mine = True
        self.hidden_image = self.mine_image
        if self.tile_size != 16:
            self.hidden_image = pygame.transform.scale(self.mine_image,(self.tile_size,self.tile_size))


    def clicked_on(self,point):
        
        if not self.rect.collidepoint(point):
            return False
        self.clicked = True
        self.image = self.hidden_image
        return True


















