# Template for the algorithm to solve a Futoshiki. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Snapshot, Cell, Futoshiki_IO


def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(200)
    Futoshiki_IO.display_puzzle(snapshot, screen)
    pygame.display.flip()

    if is_complete(snapshot):
        # for i in range

        print("returned true")
        return True

    else:
        new_snapshot = snapshot.clone()

        for solved_cell in new_snapshot.solved_cells():
            new_snapshot.remove_invalids_from_possible_list(solved_cell)

        for unsolved_cell in new_snapshot.unsolved_cells()[1:]:

            next_empty_cell_row = unsolved_cell.get_row()

            next_empty_cell_column = unsolved_cell.get_column()

            for cell_value in new_snapshot.get_cell_possibles_list(next_empty_cell_row, next_empty_cell_column):

                if check_consistency(new_snapshot, next_empty_cell_row, next_empty_cell_column, cell_value):
                    new_snapshot.set_cell_value(next_empty_cell_row, next_empty_cell_column, cell_value)

                if solve(new_snapshot, screen):
                    return True

            return False


def check_consistency(snapshot, row_for_checking, column_for_checking, value_to_test):
    for row_cell in snapshot.cells_by_row(row_for_checking):

        if row_cell.get_value() == value_to_test:
            return False

    for column_cell in snapshot.cells_by_column(column_for_checking):

        if column_cell.get_value() == value_to_test:
            return False
    return True

     
def is_complete(snapshot):
    if len(snapshot.unsolved_cells()) == 1:
        return True
    else:
        return False



