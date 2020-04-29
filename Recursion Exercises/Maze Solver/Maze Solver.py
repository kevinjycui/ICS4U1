import random # Modules
import os
import pygame

'''
Communication Questions
⦁	What happens if instead of searching in the order North, East, South, West, FIND PATH searches North, South, East, West?
    The order of searching determines which directions the maze solver will traverse first. Searching in the order of [North, South, East, West] will prioritize
    North before South, South before East, etc. For example, if the path from the start to the goal happens to mostly consist of northward turns, then searching
    North first will be more optimal. However, since the maze and coordinates are pseudorandomly generated, this change in algorithm does not effect the overall
    efficiency of the FIND PATH function.

⦁	When FIND-PATH returns False, does that mean there is no path from the start to the goal?
    When one call of the FIND PATH function within the recursion stack returns False, this means that that specific direction in the path is invalid. If the entire
    function returns False, that means that every possible path is invalid and thus tehre is no path from the start to the goal.

⦁	Can parts of the maze be searched by FIND-PATH more than once? How does the algorithm deal with this situation?
    If non-wall parts of the maze can be searched by the FIND PATH function more than once, the function would form loops, going back and forth to already visited
    parts. This revisiting of parts is also unnecessary since the optimal path would only visit every part in the path once, with loops only adding distance without
    changing position. By using a matrix that holds whether each part is visited or not, the function can understand that visited paths are invalid even if they are
    not walls. Walls can be visited by multiple adjacent empty cells, but this is already dealt with as walls are already considered invalid, and the path would not
    continue to form loops after hitting a wall.

'''


def load_maze(file): # Loads maze from text file
    '''
    (str) -> (list)

    Loads maze data from a text file to a 2-dimensional list
    '''
    maze = [] # Hold maze as 2-dimensional list
    with open(file) as f:
        for i, r in enumerate(f.readlines()):
            maze.append([])
            for block in r.strip():
                maze[i].append(block) # Append chars to list
    return maze # Return matrix

def random_coordinates_generator(maze): # Generates a set of x and y coordinates on a maze in empty positions
    '''
    (list) -> (int, int)

    Returns the coordinates within a 2-dimensional that does not contain a wall
    '''
    x, y = random.randint(1, len(maze)-2), random.randint(1, len(maze[0])-2) # Gets random integers within the range
    while maze[x][y] != ' ': # Check to see if position on maze is empty
        x, y = random.randint(1, len(maze)-2), random.randint(1, len(maze[0])-2)
    return x, y # Return coordinates

# Calling initial functions
maze = load_maze('maze.txt') # Load maze

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init() # Initialize Pygame for graphics

pygame.display.set_caption('Maze solver')
screen = pygame.display.set_mode((len(maze)*10, len(maze[0])*10)) # Set size of window to size of maze

WHITE = (255, 255, 255) # Create colour constants for graphics
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
colour = {' ': WHITE, '#': BLACK, '+': BLUE, 'X': RED} # Assign position statuses to colours

startx, starty = random_coordinates_generator(maze) # Generate coordinates for start
goalx, goaly = random_coordinates_generator(maze) # Generate coordinates for goal

def print_maze(maze, final=False): # Output maze in a matrix format
    '''
    (list, boolean=False) -> (None)

    Prints the content of a maze represented by a 2-dimensional list as a matrix, final boolean determines if wrong paths are shown
    '''
    if final: # Output without showing failures
        for m in maze:
            print(''.join(m).replace('X', ' ')) # Replace closed chars with empty chars
        return
    for m in maze:
        print(''.join(m)) # Print maze

def display_window(maze): # Display window in pygame
    '''
    (list) -> (None)

    Displays the contents of a maze represented by a 2-dimensional list in the Pygame window
    '''
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == (startx, starty) or (i, j) == (goalx, goaly):                
                pygame.draw.rect(screen, GREEN, (10*i, 10*j, 10, 10)) # Draw green square at start and goal
            else:
                pygame.draw.rect(screen, colour[maze[i][j]], (10*i, 10*j, 10, 10)) # Draw assigned colour square at every other position
    pygame.display.flip()
    
    for e in pygame.event.get(): # Check for events to create response
        if e.type == pygame.QUIT:
            pygame.quit() # Check for window quit
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()

def find_path(maze, start, goal): # Recursive maze solver
    '''
    (list, (int, int), (int, int)) -> boolean

    Recursively searches for a path from the start coordinate to the goal coordinate in the maze matrix
    '''
    x, y = start # Get current position
    if start == goal: # Return True if goal reached
        return True
    if maze[x][y] == '#' or maze[x][y] == 'X' or maze[x][y] == '+': # Check if current position is invalid
        return False
    maze[x][y] = '+' # Set position as path

    display_window(maze) # Display updated window
    
    if find_path(maze, (x-1, y), goal) or find_path(maze, (x, y+1), goal) or find_path(maze, (x+1, y), goal) or find_path(maze, (x, y-1), goal):
        return True # Check 4 directions to continue path

    maze[x][y] = 'X' # Set as invalid if path failed

    display_window(maze) # Display updated window

    return False

find_path(maze, (startx, starty), (goalx, goaly)) # Call maze solver
maze[startx][starty] = 'S' # Set start as S char
maze[goalx][goaly] = 'G' # Set goal as G char
print_maze(maze) # Output maze with failures
print('\nFinal path solution:')
print_maze(maze, 1) # Output maze with only solution

run = True
while run: # Keep window running until exited by user
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False

pygame.quit() # Quit pygame
