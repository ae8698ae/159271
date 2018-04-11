import pygame
import random

print("Alex Binns 07185952")
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size = [1000, 1000]
screen = pygame.display.set_mode(size)
# Set the screen background
screen.fill(white)
      
# Set title of screen
pygame.display.set_caption("Random Maze")
 
# Create a 2 dimensional array. A two dimensional
# array in our implementation is simply a list of lists.
# Each cell corresponds to a 5 pixel x 5 pixel area of the screen surface.
maze_grid = []
for x_coordinate in range(200):
    # Add an empty array that will hold each cell in this row
    maze_grid.append([])
    for y_coordinate in range(200):
        maze_grid[x_coordinate].append(0)  # Append a cell


# code to be implemented
def generate_maze():
    # draw the left outside wall
    left_wall = maze_grid[0]
    for i in range(len(left_wall)):
        left_wall[i] = 1

    # draw the right outside wall
    right_wall = maze_grid[(len(maze_grid) - 1)]
    for i in range(len(right_wall)):
        right_wall[i] = 1

    # draw the top and bottom outside walls
    for i in range(len(maze_grid)):
        maze_grid[i][0] = 1
        maze_grid[i][(len(maze_grid) - 1)] = 1

    # draw the door at the top left
    maze_grid[0][0] = 0
    maze_grid[0][1] = 0
    maze_grid[1][0] = 0
    maze_grid[1][1] = 0

    # call function to draw the rest of the maze
    add_walls(maze_grid, ((0, 0), (len(maze_grid) - 1, len(maze_grid) - 1)), True)


def add_walls(maze_grid, room_coordinates, cheese_flag):
    # set the coordinates for the top and bottom from the input coordinates
    low_x = room_coordinates[0][0]
    low_y = room_coordinates[0][1]
    high_x = room_coordinates[1][0]
    high_y = room_coordinates[1][1]

    # Base case to return if the room is less than 5
    if (high_y - low_y) < 5 or (high_x - low_x) < 5:
        # set the location of the cheese if the cheese_flag is true
        if cheese_flag:
            maze_grid[((high_x + low_x) // 2)][((high_y + low_y) // 2)] = 2
        return

    else:
        # set the random location for the vertical and horizontal dividers
        vertical_line = random.randint(low_x + 2, high_x - 2)
        horizontal_line = random.randint(low_y + 2, high_y - 2)

        # set the horizontal and vertical lines in the array
        for i in range(low_x, high_x + 1):
            maze_grid[i][horizontal_line] = 1
        for i in range(low_y, high_y + 1):
            maze_grid[vertical_line][i] = 1

        # change the coordinates for the door back to white
        maze_grid[vertical_line][horizontal_line] = 0
        maze_grid[(vertical_line + 1)][horizontal_line] = 0
        maze_grid[(vertical_line - 1)][horizontal_line] = 0
        maze_grid[vertical_line][(horizontal_line + 1)] = 0
        maze_grid[vertical_line][(horizontal_line - 1)] = 0

        # call recursive function on the top left room
        add_walls(maze_grid, ((low_x, low_y), (vertical_line, horizontal_line)), False)

        # set the location of the cheese if the cheese_flag is true
        if cheese_flag:
            # choose random number to choose next location for the cheese
            cheese_locator = random.randint(1, 3)

            if cheese_locator == 1:
                add_walls(maze_grid, ((vertical_line, low_y), (high_x, horizontal_line)), True)
                add_walls(maze_grid, ((low_x, horizontal_line), (vertical_line, high_y)), False)
                add_walls(maze_grid, ((vertical_line, horizontal_line), (high_x, high_y)), False)

            elif cheese_locator == 2:
                add_walls(maze_grid, ((vertical_line, low_y), (high_x, horizontal_line)), False)
                add_walls(maze_grid, ((low_x, horizontal_line), (vertical_line, high_y)), True)
                add_walls(maze_grid, ((vertical_line, horizontal_line), (high_x, high_y)), False)

            else:
                add_walls(maze_grid, ((vertical_line, low_y), (high_x, horizontal_line)), False)
                add_walls(maze_grid, ((low_x, horizontal_line), (vertical_line, high_y)), False)
                add_walls(maze_grid, ((vertical_line, horizontal_line), (high_x, high_y)), True)

        # if cheese_flag is false call the function on the remaining rooms with a false flag
        else:
            add_walls(maze_grid, ((vertical_line, low_y), (high_x, horizontal_line)), False)
            add_walls(maze_grid, ((low_x, horizontal_line), (vertical_line, high_y)), False)
            add_walls(maze_grid, ((vertical_line, horizontal_line), (high_x, high_y)), False)


def display_maze():
    for row_to_draw in range(len(maze_grid)):
        for column_to_draw in range(len(maze_grid[row_to_draw])):
            if maze_grid[row_to_draw][column_to_draw] == 0:
                cell_colour = white
            elif maze_grid[row_to_draw][column_to_draw] == 2:
                cell_colour = yellow
            else:
                cell_colour = black
            pygame.draw.rect(screen, cell_colour, ((column_to_draw * 5), (row_to_draw * 5), 5, 5), 0)


# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done is False:
    for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:  # If user wants to perform an action
                if event.key == pygame.K_m:
                    generate_maze()
                    display_maze()

    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit()
