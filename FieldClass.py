# -*- coding: utf-8 -*-

class Field:
    def __init__(self, rows):
        self.rows = rows
        self.columns = [list(i) for i in zip(*zip(*zip(*rows[::-1])[::-1])[::-1])] #Sometimes you do what you gotta do
        self.length = len(rows)                                                    #I needed a matrix rotated anti-clockwise
        
    def __getitem__(self, data):
        index, is_row = data
        if is_row:
            return self.rows[index]
        else:
            return self.columns[index]
        
    def mark_field(self, x, y, num, is_row):
        if not(is_row):
            self.rows[y][len(self.rows)-1-x] = num
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
            self.check_threes(v, i, False)
                 
    def check_threes(self, array, location, is_row):
        for index, value in enumerate(array[:-2]):
            if value == '0':
                continue
            elif value == array[index+1]:
                try:
                    #print str(location), str(index+2)
                    #print str(location), str(index-1)
                    self.mark_field(location, index+2, other(value), is_row)
                    self.mark_field(location, index-1, other(value), is_row)
                except IndexError: #At start of row/column
                    continue
            elif value == array[index+2] and array[index+1]=='0':
                self.mark_field(location, index+1, other(value), is_row)
                
    def done(self):
        for i, v in enumerate(self.rows):
            if self.is_full(v):
                continue
            
    def display_field_rows(self):
        for i in self.rows:
            for j in i:
                print j,
            print "\n"
            
    def display_field_columns(self): #Basically for testing purposes only
        for i in self.columns:
            for j in i:
                print j,
            print "\n"
            
    def reset_columns(self):
        self.columns = [list(i) for i in zip(*zip(*zip(*self.rows[::-1])[::-1])[::-1])]
        
    def check_num(self, array, index, is_row):
        if self.is_full(array):
            return "done"
        elif array.count('1') == len(array)/2: #len(array) should always be even so I don't have to check integer division
            for i, v in enumerate(array):
                if v == '0':
                    self.mark_field(index, i, '2', is_row)
        elif array.count('2') == len(array)/2:
            for i, v in enumerate(array):
                if v == '0':
                    self.mark_field(index, i, '1', is_row)
                    
    def all_row_num(self):
        for i, v in enumerate(self.rows):
            self.check_num(v, i, True)
            
    def all_column_num(self):
        for i, v in enumerate(self.columns):
            self.check_num(v, i, False)
        
def other(value):
    if value == '1':
        return '2'
    return '1'
    
                    
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
field.display_field_rows()
for i in range(10):
    field.all_row_threes()
    field.all_column_threes()
    field.all_row_num()
    field.all_column_num()
print "========================"
field.display_field_rows()