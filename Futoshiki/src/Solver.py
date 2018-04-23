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

    # check if the puzzle is complete
    if is_complete(snapshot):
        if check_consistency(snapshot):
            print("returned true")
            return True
        else:
            print("returned false")
            return False

    else:
        new_snapshot = snapshot.clone()

        for solved_cell in snapshot.solved_cells():
            snapshot.remove_invalids_from_possible_list(solved_cell)

        new_snapshot.remove_constraints()

        # check each cell in the list of unsolved cells
        for unsolved_cell in new_snapshot.unsolved_cells():
            unsolved_cell_row = unsolved_cell.get_row()
            unsolved_cell_column = unsolved_cell.get_column()

            # check each possible value if it is valid for the unsolved cell
            for cell_value in unsolved_cell.get_possible_values():
                # if the consistency is true then set the cell value and do a recursive call
                if check_consistency(new_snapshot, unsolved_cell_row, unsolved_cell_column, cell_value):
                    new_snapshot.set_cell_value(unsolved_cell_row, unsolved_cell_column, cell_value)
                    if solve(new_snapshot, screen):
                        return True
            # return False if we have reached here as there is no possible solution for this tree
            return False



def check_consistency(snapshot):
    for row in range(6):
        for row_cell in snapshot.cells_by_row(row):
            value_to_test = row_cell.get_value()
            for row_cell_to_test in snapshot.cells_by_row(row):
                if row_cell_to_test.get_value() == value_to_test:
                    return False

    for column in range(6):
        for column_cell in snapshot.cells_by_column(column):
            value_to_test = column_cell.get_value()
            for column_cell_to_test in snapshot.cells_by_column(column):
                if column_cell_to_test.get_value() == value_to_test:
                    return False
    return True


def check_consistency_cell(snapshot, row_for_checking, column_for_checking, value_to_test):
    for row_cell in snapshot.cells_by_row(row_for_checking):
        if row_cell.get_value() == value_to_test:
            return False

    # check that the cell value is not the same as any other cell in the column return false if there is
    for column_cell in snapshot.cells_by_column(column_for_checking):
        if column_cell.get_value() == value_to_test:
            return False

    # check that the value conforms with the constraints return false if it doesn't
    cell_for_checking = (row_for_checking, column_for_checking)
    for constraint in snapshot.get_constraints():
        if cell_for_checking in constraint:
            if cell_for_checking == constraint[0]:
                if snapshot.get_cell_value(constraint[1][0], constraint[1][1]) != 0:
                    if value_to_test > snapshot.get_cell_value(constraint[1][0], constraint[1][1]):
                        return False
            elif cell_for_checking == constraint[1]:
                if snapshot.get_cell_value(constraint[0][0], constraint[0][1]) != 0:
                    if value_to_test < snapshot.get_cell_value(constraint[0][0], constraint[0][1]):
                        return False

    # return true if it passes all the tests
    return True


# function that returns true if the puzzle is complete
def is_complete(snapshot):
    return snapshot.unsolved_cells() == []
