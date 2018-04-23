# This is a cell in a Futoshiki, consisting of x, y coordinates (column and row) and a value. 
# All parameters are integers between 1..5, values can also be 0 indicating that the value is still unknown.


class Cell:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.possible_values = [1, 2, 3, 4, 5]
        self.constraints = []
        
    def get_row(self):
        return self.row
    
    def set_row(self, row):
        self.row = row
        
    def get_column(self):
        return self.column
    
    def set_column(self, col):
        self.column = col
        
    def get_value(self):
        return self.value
    
    def set_value(self, val):
        self.value = val
        
    def clone(self): 
        return Cell(self.row, self.column, self.value)

    def get_possible_values(self):
        return self.possible_values

    def remove_from_possible(self, value):
        self.possible_values.remove(value)

