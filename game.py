import pygame,sys


# 8 by 8 16 by 16 -> 16 by 30

# 32 pixel gap at top
# 32 + 16 * 8

screen_width = screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
BLACK = (0,0,0)


def game():
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        

        pygame.display.update()




def menu():


    title_font = pygame.font.SysFont("comicsansms",80)

    title_text = title_font.render("MINESWEEPER",True,BLACK)

    top_gap = 30





















