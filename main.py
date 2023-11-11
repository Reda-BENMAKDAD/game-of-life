# my own implementation of conway's game of life because...why not ?

##################################### PROGRESS ############################################################         
# progress:                                                                                               #
# it would be good if i implemented a camera to be able to follow evolution of "beings"                   #
# make an feature where the user can draw the first generation of cells, and lunch the game from there    #
###########################################################################################################
# imports
import pygame
pygame.init()
from argparse import ArgumentParser
from random import randint
from time import sleep
from math import floor
import keyboard

############ initializing some default values if the user doesn't specify them #################à
# monitor info for default values
MONITOR_W, MONITOR_H = pygame.display.Info().current_w, pygame.display.Info().current_h
# the screen height is set to 2/3 of the monitor height by default and same fo screen width
TWO_THIRDS_SCREEN_HEIGHT      = floor(MONITOR_H*(2/3)) # we will set these to be divisible by 10 since default values of screen width and height are 10
TWO_THIRDS_SCREEN_WIDTH       = floor(MONITOR_W)*(2/3)
DEFAULT_SCREEN_HEIGHT         = int(TWO_THIRDS_SCREEN_HEIGHT - (TWO_THIRDS_SCREEN_HEIGHT%10))
DEFAULT_SCREEN_WIDTH          = int(TWO_THIRDS_SCREEN_WIDTH - (TWO_THIRDS_SCREEN_WIDTH%10))
default_resolution_of_screen  = int(DEFAULT_SCREEN_HEIGHT * DEFAULT_SCREEN_WIDTH)
DEFAULT_NUMBER_OF_CELLS       = int((DEFAULT_SCREEN_HEIGHT/10) * (DEFAULT_SCREEN_WIDTH/10))

# the settings for the screen and cells...will be controlled from the command line
parser = ArgumentParser(description="my implementation of conway's game of life")
parser.add_argument("-sw", "--screen-width"   ,type=int    ,metavar=''   ,help="the screen width"                              ,default=DEFAULT_SCREEN_WIDTH)
parser.add_argument("-sh", "--screen-height"  ,type=int    ,metavar=''   ,help="the screen height"                             ,default=DEFAULT_SCREEN_HEIGHT)
parser.add_argument("-cw", "--cell-width"     ,type=int    ,metavar=''   ,help="the width of each individual cell"             ,default=10)
parser.add_argument("-ch", "--cell-height"    ,type=int    ,metavar=''   ,help="the height of each individual cell"            ,default=10)
parser.add_argument("-a" , "--alive"          ,type=int    ,metavar=''   ,help="number of cells alive at the start of the game",default=randint(int((1/2)*DEFAULT_NUMBER_OF_CELLS  ), int((3/4)*DEFAULT_NUMBER_OF_CELLS  )))
parser.add_argument("-f" , "--fps"            ,type=float  ,metavar=''   ,help="you could see this as the speed of the game, or how much time will a generation be shown on the screen", default=1)
args = parser.parse_args()



# showing game parameters to user
print(f"""############ game parameters #######################
screen height: {args.screen_height}
screen width: {args.screen_width}
cell height: {args.cell_height}
cell width: {args.cell_width}
total number of cells: {int((args.screen_height/args.cell_height) * (args.screen_width/args.cell_width))}
alive cells at start: {args.alive}
fps: {args.fps}

####################################################
""")

# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# screen settings
WIDTH, HEIGHT= args.screen_width, args.screen_height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.update()
print("performing necessary calculations...please wait")
# clock
clock = pygame.time.Clock()
FPS = args.fps

# cell settings
CELL_WIDTH, CELL_HEIGHT = args.cell_width, args.cell_height
# height and width of screen should be divisible respectively by cell's height and width
NUMBER_OF_CELLS = (HEIGHT/CELL_HEIGHT) * (WIDTH/CELL_WIDTH)



# generating two dimensional array of cells that represents cells in a grid
CELLS = []
NUMBER_OF_ALIVE_CELLS_AT_BEGGINNING = args.alive
def generate_random_number_divisible_by_ten(min, max):
    number = randint(min, max)
    number -= number%args.cell_height
    return number

# generating a random list of tuples, each tuple contains two numbers divisble by 10
alive_cells_at_start = [(generate_random_number_divisible_by_ten(0, WIDTH), generate_random_number_divisible_by_ten(0, HEIGHT)) 
                        for _ in range(NUMBER_OF_ALIVE_CELLS_AT_BEGGINNING)]


alive_or_dead = []
for y in range(0, HEIGHT, CELL_HEIGHT):
    new_line = []
    alive_or_dead_line = []
    for x in range(0, WIDTH, CELL_WIDTH):
        if (x, y) in alive_cells_at_start:
            alive_or_dead_line.append(1)
        else:
            alive_or_dead_line.append(0)
        new_line.append(pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT))
    alive_or_dead.append(alive_or_dead_line)
    CELLS.append(new_line)

def new_generation():
    for index, line in enumerate(alive_or_dead):
        for index2, cell in enumerate(line):
            # dealing with cells in the corners since they don't have full 6 neighbots ####################################
            if index==0 and index2==0:
                neighbors = [alive_or_dead[index][index2+1],
                alive_or_dead[index][index2+1], alive_or_dead[index+1][index2+1]]
            
            elif index==0 and index2==len(line)-1:
                neighbors = [alive_or_dead[index][index2-1],
                             alive_or_dead[index+1][index2-1],
                             alive_or_dead[index+1][index2]]
            
            elif index==len(alive_or_dead)-1 and index2==0 :
                neighbors = [alive_or_dead[index-1][index2],
                            alive_or_dead[index-1][index2+1],
                            alive_or_dead[index][index2+1]]
            elif index==len(alive_or_dead)-1 and index2==len(line)-1:
                neighbors = [alive_or_dead[index-1][index2],
                             alive_or_dead[index-1][index2-1],
                             alive_or_dead[index], index2-1]
            
           
            elif index==len(alive_or_dead)-1:
                neighbors = [alive_or_dead[index-1][index2-1],  alive_or_dead[index][index2-1],
                            alive_or_dead[index-1][index2]  ,  alive_or_dead[index][index2+1],
                            alive_or_dead[index-1][index2+1],  alive_or_dead[index][index2+1]]
            ###############################################################################################################

            ##### dealing with cells in the edge lines (and not in the corners) ###########################################
            elif index2==0:
                neighbors = [alive_or_dead[index-1][index2]  ,  alive_or_dead[index][index2+1],
                            alive_or_dead[index-1][index2+1],  alive_or_dead[index][index2+1], alive_or_dead[index+1][index2+1]]
            
    
            elif index2==len(line)-1:
                neighbors = [alive_or_dead[index-1][index2-1],  alive_or_dead[index][index2-1], alive_or_dead[index+1][index2],
                            alive_or_dead[index-1][index2]  ,  alive_or_dead[index+1][index2-1]]
            
            elif index2==0:
                neighbors = [
                            alive_or_dead[index-1][index2]  ,  alive_or_dead[index][index2+1],
                            alive_or_dead[index-1][index2+1],  alive_or_dead[index+1][index2], alive_or_dead[index+1][index2+1]]
            ################################################################################################################
            
            ##### the rest of the cases ####################################################################################
            else:
                neighbors = [alive_or_dead[index-1][index2-1],  alive_or_dead[index][index2-1], alive_or_dead[index+1][index2-1],
                            alive_or_dead[index-1][index2]  ,  alive_or_dead[index][index2+1],  alive_or_dead[index+1][index2],
                            alive_or_dead[index-1][index2+1],                                   alive_or_dead[index+1][index2+1]]

            if cell==1 and neighbors.count(1) < 2:
                kill_cell((index, index2))
            elif cell==1 and neighbors.count(1) ==2 or neighbors.count(1) == 3:
                alive_cell((index, index2))
            elif cell==0 and neighbors.count(1)>3:
                kill_cell((index, index2))
            else:
                kill_cell((index, index2))

               


    


# turns a cell to white color to represent that it died
def kill_cell(coordinates):
    alive_or_dead[coordinates[0]][coordinates[1]] = 0

# opposite of kill_cell
def alive_cell(coordinates):
    alive_or_dead[coordinates[0]][coordinates[1]] = 1

def draw_grid(CELLS):
    for index, line in enumerate(CELLS):
        for index2, cell in enumerate(line):
            pygame.draw.rect(screen, BLACK if alive_or_dead[index][index2] else WHITE, cell)

draw_grid(CELLS)
print("starting game")
pygame.display.update()
sleep(1)

while True:
    if pygame.event.get(pygame.QUIT):
        break
    
    new_generation()
    draw_grid(CELLS)
    pygame.display.update()
    clock.tick(FPS)
 
pygame.quit()
