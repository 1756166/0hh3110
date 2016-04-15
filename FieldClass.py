# -*- coding: utf-8 -*-

class Field:
    def __init__(self, rows):
        self.rows = rows
        self.columns = [list(i) for i in zip(*zip(*zip(*rows[::-1])[::-1])[::-1])] #Sometimes you do what you gotta do
        self.length = len(rows)                                                    #I needed a matrix rotated anti-clockwise
        
    def __getitem__(self, data): #This allows me to access a specific row/column using the same syntax
        index, is_row = data
        if is_row:
            return self.rows[index]
        else:
            return self.columns[index]
        
    def mark_field(self, x, y, num, is_row):
        if not(is_row):
            self.rows[y][x] = num
        else:
            self.rows[x][y] = num
        self.reset_columns()
        
    def is_full(self, array):
        return not(any([i=='0' for i in array]))
           
    def all_row_threes(self):
        for i, v in enumerate(self.rows):
            self.check_threes(v, i, True)
            
    def all_column_threes(self):
        for i, v in enumerate(self.columns):
            self.check_threes(v, i, True)
                 
    def check_threes(self, array, location, is_row):
        for index, value in enumerate(array[:-2]):
            if value == '0':
                continue
            elif value == array[index+1]:
                try:
                    self.mark_field(location, index+2, other(value), is_row)
                    self.mark_field(location, index-1, other(value), is_row)
                except IndexError: #At start of row/column
                    continue
            elif value == array[index+2] and array[index+1]=='0':
                self.mark_field(location, index+1, other(value), is_row)
                
    def all_rows_full(self):
        for i, v in enumerate(self.rows):
            if self.is_full(v):
                continue
            
    def all_columns_full(self):
        for i,v in enumerate(self.columns):
            if self.is_full(v):
                continue
            
    def display_field_rows(self):
        for i in self.rows:
            for j in i:
                print j,
            print "\n"
            
    def display_field_columns(self):
        for i in self.columns:
            for j in i:
                print j,
            print "\n"
            
    def reset_columns(self):
        self.columns = [list(i) for i in zip(*zip(*zip(*self.rows[::-1])[::-1])[::-1])]
def other(value):
    if value == '1':
        return '2'
    return '1'
    
def check_num(field, array, is_row, index, num): #Same input as check_three
    print array.count('1')
    print array.count('2')
    if array.count('1')+array.count('2')==len(array):
        return field
    if array.count(num)==len(array)/2: #that number is full, we can fill with other
        for i,v in enumerate(array):
            if v == '0':
                if is_row:
                    field = field.mark_field(field, index, i, other(num))
                else:
                    field = field.mark_field(field, i, index, other(num))
                    
    return field
                    
field = '''
0 0 0 0 0 2 0 0 0 0 0 0
2 0 0 0 1 0 0 0 0 0 0 1
0 0 1 0 0 0 1 0 0 2 0 1
0 0 1 1 0 0 1 0 0 0 0 0
2 0 0 0 0 2 2 1 2 1 0 2
0 0 0 0 0 2 1 0 2 0 0 0
0 1 2 0 0 0 0 1 1 0 0 2
1 2 0 1 0 0 1 1 0 1 1 2
0 1 0 0 0 1 0 0 0 0 2 0
0 0 0 0 0 0 1 1 0 1 0 0
2 0 0 2 0 0 0 0 0 0 0 2
1 0 0 0 0 0 0 2 2 0 0 0'''.split('\n')
field = [i.split() for i in field[1:]]
field = Field(field)