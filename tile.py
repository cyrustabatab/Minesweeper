import pygame,os


def get_mapping_number_to_image():
    
    mapping = {}
    for number in range(1,9):

        mapping[number] = pygame.image.load(os.path.join('assets',f"{number}.png")).convert_alpha()

    return mapping









class Tile(pygame.sprite.Sprite):

    block_image = pygame.image.load(os.path.join('assets','block.png'))
    mine_image = pygame.image.load(os.path.join('assets','mine.png'))
    empty_image = pygame.image.load(os.path.join('assets','empty.png'))
    flag_image =pygame.image.load(os.path.join('assets','flagged.png'))

    number_to_image = get_mapping_number_to_image()


    def __init__(self,x,y,row,col,tile_size=16):
        super().__init__()
        self.x = x
        self.y = y
        self.row = row
        self.col = col
        self.tile_size = tile_size
        self.hidden_image = self.empty_image
        if tile_size != 16:
            self.block_image = pygame.transform.scale(self.block_image,(tile_size,tile_size))
            self.hidden_image = pygame.transform.scale(self.hidden_image,(tile_size,tile_size))
            self.flag_image = pygame.transform.scale(self.flag_image,(tile_size,tile_size))
        
        self.image = self.block_image

        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.is_mine = False
        self.clicked = False
        self.flagged = False
        self.neighboring_mines = 0
    

    def reset_image(self):
        self.image = self.block_image

    def mark_mine(self):
        self.is_mine = True
        self.hidden_image = self.mine_image
        if self.tile_size != 16:
            self.hidden_image = pygame.transform.scale(self.hidden_image,(self.tile_size,self.tile_size))
    

    def set_number(self,number):

        self.neighboring_mines = number
        if number in self.number_to_image:
            self.hidden_image = self.number_to_image[number]
        else:
            self.hidden_image = self.empty_image
        if self.tile_size != 16:
            self.hidden_image = pygame.transform.scale(self.hidden_image,(self.tile_size,self.tile_size))

    def clicked_on(self,point):
        if self.flagged or self.clicked or not self.rect.collidepoint(point):
            return False
        self.clicked = True
        self.image = self.hidden_image
        return True
    
    def uncover(self):
        self.clicked = True
        self.image = self.hidden_image

    def set_flag(self,point):
        if self.clicked or not self.rect.collidepoint(point):
            return False

        if self.flagged == True:
            self.image = self.block_image
            self.flagged = False
        else:
            self.flagged = True
            self.image = self.flag_image
        return True




















