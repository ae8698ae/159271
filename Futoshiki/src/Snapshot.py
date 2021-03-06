# A snapshot is a point in the computation when 
# the values for some, but possibly not all, cells are known.
# This class has some methods that allow to clone a snapshot (this is useful to produce the 
# next snapshots in the recursion tree), to query the cells in various ways, and to set cells.
# It also has a method that returns a list encoding the inequality constraints that must be satisfied.

import Cell


class Snapshot:
    def __init__(self):
        self.rows = 5
        self.columns = 5
        self.cells = []
        for row in range(5):
            # Add an empty array that will hold each cell in this row
            self.cells.append([])
            for column in range(5):
                self.cells[row].append(Cell.Cell(row, column, 0))  # Append a cell
        self.constraints = []
        
    def set_cell_value(self, row, column, value):
        self.cells[row][column].set_value(value)
        
    def get_cell_value(self, row, column):
        return self.cells[row][column].get_value()

    def set_cell_constraint(self, row, column, greater_or_less_than, cell):
        self.cells[row][column].constraints.append([greater_or_less_than, cell])

    def get_cell_possibles_list(self, row, column):
        return self.cells[row][column].possible_values

    def set_constraint(self, coords):
        self.constraints.append(coords)
    
    def get_constraints(self):
        constraints = []  
        for constraint_coordinate_set in self.constraints:
            lesser = (constraint_coordinate_set[0], constraint_coordinate_set[1])
            greater = (constraint_coordinate_set[2], constraint_coordinate_set[3])
            constraints.append((lesser, greater))
        return constraints
        
    def cells_by_row(self, row):
        return self.cells[row]
    
    def cells_by_column(self, col):
        column = []
        for row in range(5):
            column.append(self.cells[row][col])
        return column
    
    def unsolved_cells(self):
        unsolved = [0]
        for row in range(5):
            for column in range(5):
                if self.cells[row][column].get_value() == 0:
                    unsolved.append(self.cells[row][column])
        self.heapify(unsolved)
        return unsolved

    def solved_cells(self):
        solved = []
        for row in range(5):
            for column in range(5):
                if self.cells[row][column].get_value() != 0:
                    solved.append(self.cells[row][column])
        return solved
        
    def clone(self):
        clone = Snapshot()
        for row in range(5):
            for col in range(5):
                clone.set_cell_value(row, col, self.get_cell_value(row, col))
        for c in self.constraints:     
            clone.set_constraint(c)
        return clone

    def remove_invalids_from_possible_list(self, cell):
        value_to_remove = cell.get_value()
        cell_coordinates = (cell.get_row(), cell.get_column())

        for row_cell in self.cells_by_row(cell_coordinates[0]):
            if row_cell != cell:
                try:
                    row_cell.possible_values.remove(value_to_remove)
                except ValueError:
                    pass

        for column_cell in self.cells_by_column(cell_coordinates[1]):
            if column_cell != cell:
                try:
                    column_cell.possible_values.remove(value_to_remove)
                except ValueError:
                    pass

        for constraint in self.get_constraints():
            if cell_coordinates == constraint[0]:
                for i_to_remove in range(1, value_to_remove + 1):
                    try:
                        self.cells[constraint[1][0]][constraint[1][1]].possible_values.remove(i_to_remove)
                    except ValueError:
                        pass
            if cell_coordinates == constraint[1]:
                for i_to_remove in range(value_to_remove, 6):
                    try:
                        self.cells[constraint[0][0]][constraint[0][1]].possible_values.remove(i_to_remove)
                    except ValueError:
                        pass

    def heapify(self, a_list):
        list_length = len(a_list) - 1
        for j in range(list_length // 2, 0, -1):
            self.siftdown(a_list, j, list_length)

    def siftdown(self, list_for_sorting, index, list_length):
        temp = list_for_sorting[index]
        # check if there is a child by multiplying the index by 2 and checking if it is less than the last index
        while 2 * index <= list_length:
            child = 2 * index
            # check if there is a right child and if it is bigger than the left child
            if (child < list_length) and (len(list_for_sorting[child + 1].possible_values) <
                                          len(list_for_sorting[child].possible_values)):
                child = child + 1
            # if the child is higher than the original if so put the child in the position of the original
            if len(list_for_sorting[child].possible_values) < len(temp.possible_values):
                list_for_sorting[index] = list_for_sorting[child]
            else:
                break  # exit while loop if it not higher
            index = child
        # insert original list[index] in correct spot
        list_for_sorting[index] = temp
