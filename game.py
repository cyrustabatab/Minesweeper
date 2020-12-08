import pygame,sys

pygame.init()
# 8 by 8 16 by 16 -> 16 by 30

# 32 pixel gap at top
# 32 + 16 * 8

screen_width , screen_height =1500, 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (220,220,220)



def game():

    global screen
    screen_width = screen_height = 400
    screen = pygame.display.set_mode((screen_width,screen_height))
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        

        pygame.display.update()




def menu():
    global screen
    
    menu_width,menu_height = screen_width,screen_height
    title_font = pygame.font.SysFont("comicsansms",80)

    title_text = title_font.render("MINESWEEPER",True,BLACK)

    top_gap = 30

    title_text_x,title_text_y = screen_width//2 - title_text.get_width()//2,top_gap
    
    gap = 50

    easy_text = title_font.render("EASY",True,BLACK,RED)
    medium_text = title_font.render("MEDIUM",True,BLACK,RED)
    hard_text = title_font.render("HARD",True,BLACK,RED)

    
    gap_between_buttons = 50

    medium_text_x,medium_text_y = menu_width//2 - medium_text.get_width()//2,title_text_y + title_text.get_height() + gap

    easy_text_x,easy_text_y = medium_text_x - gap_between_buttons - easy_text.get_width(),title_text_y + title_text.get_height() + gap
    hard_text_x,hard_text_y = medium_text_x + medium_text.get_width() + gap_between_buttons,title_text_y + title_text.get_height() + gap

    

    def draw_menu():
        screen.fill(GRAY)
        screen.blit(title_text,(title_text_x,title_text_y))

        screen.blit(easy_text,(easy_text_x,easy_text_y))
        screen.blit(medium_text,(medium_text_x,medium_text_y))
        screen.blit(hard_text,(hard_text_x,hard_text_y))

    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game()
                screen = pygame.display.set_mode((menu_width,menu_height))

        

        
        draw_menu()
        pygame.display.update()





if __name__ == "__main__":
    menu()

















