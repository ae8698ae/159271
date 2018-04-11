# Utility to read Futoshiki puzzles from text files, and display Futoshiki puzzles to a screen.

import Snapshot
import pygame


# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# This sets the width and height of each grid location
width = 60
height = 60
 
# This sets the margin between each cell
margin = 30


def load_puzzle(puzzle_file):
    file = open(puzzle_file)
    content = file.readlines()
    new_snapshot = Snapshot.Snapshot()
    
    for row_number in range(5):
        new_row = [int(x) for x in content[row_number].split()]
        for column_number in range(5):
            new_snapshot.set_cell_value(row_number, column_number, new_row[column_number])
    constraints = content[5:]
    for c in constraints:
        new_constraint = [int(x) for x in c.split()]
        new_snapshot.set_constraint(new_constraint)
    file.close()
    return new_snapshot


def display_puzzle(snapshot, screen):
    # Set the screen background
    screen.fill(black)
 
    # Draw the grid squares
    color = white
    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    for row in range(5):
        for column in range(5):       
            pygame.draw.rect(screen, color, [(margin + width)*column+margin, (margin + height) * row + margin,
                                             width, height])
            print_value = snapshot.get_cell_value(row, column)
            if print_value == 0:
                label = my_font.render(".", 1, black)
            else:
                label = my_font.render(str(print_value), 1, black)
            screen.blit(label, ((margin + width) * column + margin + 25, (margin + height) * row + margin + 10))
    my_font = pygame.font.SysFont("Comic Sans MS", 50)
    for c in snapshot.get_constraints():
        r1 = c[0][0]
        c1 = c[0][1]
        r2 = c[1][0]
        c2 = c[1][1]
        if c1 < c2:
            label = my_font.render("<", 1, red)
            screen.blit(label, ((margin + width)*(c1 + 1) + 10, (margin + height) * r2 + 20))
        elif c2 < c1:
            label = my_font.render(">", 1, red)
            screen.blit(label, ((margin + width)*(c2 + 1) + 10, (margin + height) * r2 + 20))
        elif r1 < r2:
            label = my_font.render("^", 1, red)
            screen.blit(label, ((margin + width) * c1 + margin + 15, (margin + height)*(r1 + 1) - 5))
        else:
            label = my_font.render("v", 1, red)
            screen.blit(label, ((margin + width) * c1 + margin + 15, (margin + height) * (r2 + 1) - 25))
