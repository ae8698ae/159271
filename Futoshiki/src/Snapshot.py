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

    def get_cell_possibles_list(self, row, column):
        return self.cells[row][column].possible_values

    def set_constraint(self, coordinates):
        self.constraints.append(coordinates)
    
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

    # modified unsolved cells function that also sorts the list with the fewest possibilities first before returning
    def unsolved_cells(self):
        unsolved = []
        for row in range(5):
            for column in range(5):
                if self.cells[row][column].get_value() == 0:
                    unsolved.append(self.cells[row][column])
        return_sorted = self.sort(unsolved)
        return return_sorted

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

    # function that
    def remove_used_value_from_possible_list(self, cell):
        value_to_remove = cell.get_value()
        cell_row = cell.get_row()
        cell_column = cell.get_column()
        for row_cell in self.cells_by_row(cell_row):
            if row_cell.get_column() != cell_column:
                try:
                    row_cell.possible_values.remove(value_to_remove)
                except ValueError:
                    pass
        for column_cell in self.cells_by_column(cell_column):
            if column_cell.get_row() != cell_row:
                try:
                    column_cell.possible_values.remove(value_to_remove)
                except ValueError:
                    pass

    def remove_constraints(self):
        for constraints in self.get_constraints():
            lesser = constraints[0]
            lesser_value = self.cells[lesser[0]][lesser[1]].get_value()
            greater = constraints[1]
            greater_value = self.cells[greater[0]][greater[1]].get_value()
            if lesser_value != 0:
                for value_to_remove_greater in range(1, lesser_value + 1):
                    try:
                        self.cells[greater[0]][greater[1]].possible_values.remove(value_to_remove_greater)
                    except ValueError:
                        pass
            else:
                try:
                    self.cells[greater[0]][greater[1]].possible_values.remove(1)
                except ValueError:
                    pass
            if greater_value != 0:
                for value_to_remove_lesser in range(greater_value, 6):
                    try:
                        self.cells[lesser[0]][lesser[1]].possible_values.remove(value_to_remove_lesser)
                    except ValueError:
                        pass
            else:
                try:
                    self.cells[lesser[0]][lesser[1]].possible_values.remove(5)
                except ValueError:
                    pass