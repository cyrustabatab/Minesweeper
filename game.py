import pygame,sys
import random

pygame.init()

# 8 by 8, 16 by 16 -> 16 by 30
# 32 pixel gap at top
# 32 + 16 * 8

# TODO
# make it so that they can never die on first turn(switch mine with another)?
# work on game over code(right now just print game over)

screen_width , screen_height =1500, 800
screen = pygame.display.set_mode((screen_width,screen_height))
from tile import Tile
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (220,220,220)
SILVER = (192,192,192)

tile_size = 32
board_top_gap = tile_size * 4
easy_rows = easy_cols = 8
medium_rows = medium_cols = 16
hard_rows,hard_cols = 16,30
easy_mines,medium_mines,hard_mines = 10,40,99


def count_neighbor_mines(board,row,col):

    count =0
    for row_diff in (-1,0,1):
        for col_diff in (-1,0,1):
            if row_diff ==0 and col_diff == 0:
                continue
            
            try:
                if board[row + row_diff][col + col_diff].is_mine:
                    count += 1
            except:
                pass

    return count

def create_board(rows,cols,num_mines):


    board = [[Tile(col*tile_size,board_top_gap + row * tile_size,row,col,tile_size) for col in range(cols)] for row in range(rows)]
    
    
    rows_cols = [(row,col) for row in range(rows) for col in range(cols)]



    for _ in range(num_mines):
        row_col = random.choice(rows_cols)
        row,col = row_col
        board[row][col].mark_mine()

        rows_cols.remove(row_col)







    tiles = pygame.sprite.Group()
    for row in range(rows):
        for col in range(cols):
            if not board[row][col].is_mine:
                mines = count_neighbor_mines(board,row,col)
                if mines != 0:
                    board[row][col].set_number(mines)
            tiles.add(board[row][col])
    
    
    return board,tiles





def uncover_board(board,tile):
    

    def uncover_helper(board,row,col,visited):
        
        visited.add((row,col))

        for row_diff in (-1,0,1):
            for col_diff in (-1,0,1):
                if row_diff == 0 and col_diff == 0:
                    continue
                
                neighbor_row,neighbor_col = row + row_diff,col + col_diff
                if (neighbor_row,neighbor_col) not in visited:
                    if 0 <= neighbor_row < len(board) and 0 <= neighbor_col < len(board[0]):

                        tile = board[neighbor_row][neighbor_col]
                        tile.uncover()
                        if tile.neighboring_mines == 0:
                            uncover_helper(board,neighbor_row,neighbor_col,visited)




                    


    

    visited = set()
    row,col = tile.row,tile.col
    uncover_helper(board,row,col,visited)



def game(screen_width,screen_height,rows,cols,mines):

    screen = pygame.display.set_mode((screen_width,screen_height))

    board,tiles = create_board(rows,cols,mines)
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                for tile in tiles:
                    if event.button == 1:
                        if tile.clicked_on(point):
                            if tile.is_mine:
                                print("GAME OVER")
                            elif tile.neighboring_mines == 0:
                                uncover_board(board,tile)
                            break
                    elif event.button == 3:
                        if tile.set_flag(point):
                            break



        screen.fill(SILVER)
        tiles.draw(screen)
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
    medium_text_rect = medium_text.get_rect(topleft=(medium_text_x,medium_text_y))

    easy_text_x,easy_text_y = medium_text_x - gap_between_buttons - easy_text.get_width(),title_text_y + title_text.get_height() + gap
    easy_text_rect = easy_text.get_rect(topleft=(easy_text_x,easy_text_y))

    hard_text_x,hard_text_y = medium_text_x + medium_text.get_width() + gap_between_buttons,title_text_y + title_text.get_height() + gap
    hard_text_rect = hard_text.get_rect(topleft=(hard_text_x,hard_text_y))


    

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
                coordinate= pygame.mouse.get_pos()
                

                if easy_text_rect.collidepoint(coordinate):
                    game(tile_size * easy_cols,tile_size * easy_rows + board_top_gap,easy_rows,easy_cols,easy_mines)
                elif medium_text_rect.collidepoint(coordinate):
                    game(tile_size * medium_cols,tile_size * medium_rows + board_top_gap,medium_rows,medium_cols,medium_mines)
                elif hard_text_rect.collidepoint(coordinate):
                    game(tile_size * hard_cols,tile_size * hard_rows + board_top_gap,hard_rows,hard_cols,hard_mines)

                screen = pygame.display.set_mode((menu_width,menu_height))

        

        
        draw_menu()
        pygame.display.update()





if __name__ == "__main__":
    menu()

















