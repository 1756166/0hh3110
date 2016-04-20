#!/usr/bin/python
# -*- coding: utf-8 -*-

import vision
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
            if self.rows[y][len(self.rows)-1-x] != '0': #Want to minimize this as much as possible
                print str(x), str(y), str(is_row)
            self.rows[y][len(self.rows)-1-x] = num
        else:
            if self.rows[x][y] != '0':
                print str(x), str(y), str(is_row)
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
                 
    def check_threes(self, array, location, is_row, to_check=2):
        for i in range(to_check):
            if i*'1'+'0'+(to_check-i)*'1' in array:
                self.mark_field(location, array.index(i*'1'+'0'+(to_check-i)*'1')+i, '2', is_row)
            if i*'2'+'0'+(to_check-i)*'2' in array:
                self.mark_field(location, array.index(i*'2'+'0'+(to_check-i)*'2')+i, '1', is_row)
        '''if '0'+('1'*to_check) in array:
            self.mark_field(location, array.index('0'+('1'*to_check)), '2', is_row)
        if '0'+('2'*to_check) in array:
            self.mark_field(location, array.index('0'+('1'*to_check)), '1', is_row)
        if ('1'*to_check)+'0' in array:
            self.mark_field(location, array.index(('1'*to_check)+'0')+len(('1'*to_check)+'0')-1, '2', is_row)
        if ('2'*to_check)+'0' in array:
            self.mark_field(location, array.index(('2'*to_check)+'0')+len(('2'*to_check)+'0')-1, '1', is_row)
        if '101' in array: #TODO: Get this to work for different contraints (to_check being different values)
            self.mark_field(location, array.index('101')+1, '2', is_row)
        if '202' in array:
            self.mark_field(location, array.index('202')+1, '1', is_row)'''
        '''for index, value in enumerate(array[:-2]):
            if value == '0':
                if index == 9:
                    if array[index+1]==array[index+2] and array[index+1] != '0': #Very edge case
                        value = array[index+1]
                        self.mark_field(location, index, other(value), is_row)
                else:
                    continue
            elif value == array[index+1]:
                #print str(location), str(index+2)
                #print str(location), str(index-1)
                if array[index+2] == '0':
                    self.mark_field(location, index+2, other(value), is_row)
                if index != 0:
                    if array[index-1] == '0':
                        self.mark_field(location, index-1, other(value), is_row)
            elif value == array[index+2] and array[index+1]=='0':
                self.mark_field(location, index+1, other(value), is_row)'''
                
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
            
    def is_same(self, array1, array2, is_row, index1, index2):
        same = 0
        #array1 = self.__getitem__(index1, is_row) #Double check that they're the right values
        #array2 = self.__getitem__(index2, is_row)
        for i in range(len(array1)):
            if array1[i]!=array2[i] and array1[i]!='0' and array2[i]!='0': #not the same
                return 'nope'
            else:
                if array1[i] == '0' or array2[i]=='0':
                    continue
                same += 1
        if self.is_full(array1) and self.is_full(array2):
            return "done"
        if same == 10: #If it's less then we don't have enough information to immediately complete the row
            if self.is_full(array1) and not(self.is_full(array2)):
                self.mark_field(index2, array2.index('0'), other(array1[array2.index('0')]), is_row)
                self.mark_field(index2, array2.index('0'), other(array1[array2.index('0')]), is_row) #See below comment
            elif self.is_full(array2) and not(self.is_full(array1)):
                #print same
                #print array1
                #print array2
                self.mark_field(index1, array1.index('0'), other(array2[array1.index('0')]), is_row)
                self.mark_field(index1, array1.index('0'), other(array2[array1.index('0')]), is_row) #The first zero is removed, so this works
        elif same == 11:
            if self.is_full(array1) and not(self.is_full(array2)):
                self.mark_field(index2, array2.index('0'), other(array1[array2.index('0')]), is_row)
            elif self.is_full(array2) and not(self.is_full(array1)):
                self.mark_field(index1, array1.index('0'), other(array2[array1.index('0')]), is_row)
                
                
    def is_right(self): #While editting field, this is basically debugging only, and not an extensive test
        if all([row.count('1') <=len(row)/2 and row.count('2') <= len(row)/2 for row in self.rows]):
            if all([column.count('1') <= len(column)/2 and column.count('2') <= len(row)/2 for column in self.columns]):
                return True
        return False
        
    def display_for_javascript(self):
        for row in self.rows:
            print str(row) + ','
        
def other(value):
    if value == '1':
        return '2'
    return '1'
    
def loop(field):
    while True:
        temp = list(map(list, field.rows)) #This is so temp isn't changed when field.rows is
        field.all_row_threes()
        field.all_column_threes()
        field.all_row_num()
        field.all_column_num()
        if temp == field.rows:
            break

    for index1, array1, in enumerate(field.rows):
        for index2,array2 in enumerate(field.rows):
            if index1 == index2:
                continue
            field.is_same(array1, array2, True, index1, index2)

    for index1, array1, in enumerate(field.columns):
        for index2,array2 in enumerate(field.columns): #Ideally I could start this loop from index1+1, but that messes up index2, and I think this is a better solution
            if index1 == index2:
                continue
            field.is_same(array1, array2, False, index1, index2)

def do():
    field = Field(vision.get_coords())
    for i in range(5): #Number randomly chosen by me
        loop(field)
    field.display_field_rows()
    return field
board = do()

board.display_for_javascript()
