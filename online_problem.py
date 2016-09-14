
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:55:54 2016
Python 2.7

@author: Tom Dodson
"""

import copy    #for copy.deepcopy

#class to track the connected components of a matrix. The constructor must be 
# called with the row size of the matrix in question. Has two public functions:
#
# -process_row() is called once per row of the matrix in question, and updates
# the class data structures for the new row
# -get_largest_component_size() returns the size of the largest connected
# component as an integer 
#
#The class works by keeping two lists of unique component IDs - one for the
# previous row, and one for the current row (thus avoiding storing the entire 
# problem instance). The component sizes are kept in a dictionary, keyed by that
# unique ID. When process_row is called, the tracker works from left
# to right, updating the row lists and component sizes as necessary.
#
#It's not strictly necessary for this class to work on one row at a time, 
# however, by enforcing a row-at-a-time interface, we can control direction of
# the update (i.e. not random-access), which allows us to check fewer potential 
# parent components and make simplifying assumptions about merging components

class component_tracker:
    __NONE = -1
    
    def __init__(self,n):
        self.num_cols = n
        self.prev_row = [self.__NONE]*n
        self.cur_row = [self.__NONE]*n
        self.component_size = {}
        self.cur_id = 0


    # moves from left to right, adding each piece to the appropriate components
    def process_row(self,row):
        assert(len(row) == self.num_cols)
        for i in range(self.num_cols):
            if row[i]:
                self.__update_components(i)
        
        #reached the end of a row, prepare for the next row
        self.prev_row = copy.deepcopy(self.cur_row)
        self.cur_row = [self.__NONE]*self.num_cols

    def get_largest_component_size(self):
        return sorted(self.component_size.values(),reverse=True)[0]

    #since we move from left to right and top to bottom (i.e. no random access)
    # we only have to get maximum of 4 components: the three in the previous
    # row and the neighbor to the left in the current row:
    #                         A B C
    #                         D X
    def __get_bordering_components(self,ndx):
        ids = set()
                
        if(ndx != self.num_cols-1):
            ids.add(self.prev_row[ndx+1])
        
        if(ndx != 0):
            ids.add(self.prev_row[ndx-1])
            ids.add(self.cur_row[ndx-1])
        
        ids.add(self.prev_row[ndx])
        
        return ids.difference({self.__NONE})


    #merges the component merge_id into the component keep_id
    def __merge_components(self, keep_id, merge_id, ndx):
        #iterate through the previous row and update the ids - necessary for
        # the case where a component is branched, e.g, we are currently
        # processing X:
        # 0 A 0 B 0 A 0 0      ------->    0 B 0 B 0 B 0 0
        # 0 0 X - - - - -                  0 0 B - - - - -   
        #
        #  (X <- B is actually set by the parent function, __update_components)
        for i in range(self.num_cols):
            if self.prev_row[i] == merge_id:
                self.prev_row[i] = keep_id

        # only need to iterate through the current row until the 
        for i in range(ndx):
            if self.cur_row[i] == merge_id:
                self.cur_row[i] = keep_id
                
        assert(keep_id in self.component_size)
        assert(merge_id in self.component_size)
        self.component_size[keep_id] += self.component_size[merge_id]

        #not strictly necessary, since the merged size will always be larger,
        # but better to keep the data structure clean        
        del self.component_size[merge_id]   


    def __update_components(self,ndx):
        #get component ids which border this cell
        ids = self.__get_bordering_components(ndx);
        
        #if we got no bordering component IDs, start a new component
        #if we got only one bordering component ID, simply add this position
        # to the component
        #however, if we got multiple component ids, we need to merge the
        # components
        if len(ids) == 0:
            self.cur_row[ndx] = self.cur_id;
            self.component_size[self.cur_id] = 1
            self.cur_id += 1
        elif len(ids) >= 1:
            this_id = ids.pop()
            self.cur_row[ndx] = this_id;
            
            assert(this_id in self.component_size)
            self.component_size[this_id] += 1
            
            #this is the merge case - the geometry of this solution makes it
            # impossible to merge more than two components
            if len(ids) :
                assert(len(ids) == 1)
                merge_id = ids.pop()
                self.__merge_components(this_id,merge_id,ndx)

# Safe read of integer from stdin
def read_int():
    x = None
    while not x:
        try:
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'
    return x

#reads a row from stdin and returns a list of integers
def read_row():
    row = []
    s = raw_input()
    
    num_strs = s.strip().split()    
    for i in range(len(num_strs)):
        row.append(int(num_strs[i]))
    
    return row


#read number of rows and columns
m = read_int()
n = read_int()

assert(m != None and n != None)

#create an instance of the component tracker to solve the problem                
tracker = component_tracker(n)

#read each row, then process it
for i_row in range(m):
    row = read_row()
    assert(n == len(row))    
    
    tracker.process_row(row)

#print tracker.component_size
print tracker.get_largest_component_size()


