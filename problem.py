
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:55:54 2016
Python 2.7

@author: Tom Dodson
"""


import copy

class component_tracker:
    _NONE = -1
    
    def __init__(self,n):
        self.num_cols = n
        self.prev_row = [self._NONE]*n
        self.cur_row = [self._NONE]*n
        self.component_size = {}
        self.cur_id = 0


    # moves from left to right, adding each piece to the appropriate components
    def process_row(self,row):
        assert(len(row) == self.num_cols)
        for i in range(self.num_cols):
            if row[i]:
                self.update_components(i)
        
        #reached the end of a row, prepare for the next row
        self.prev_row = copy.deepcopy(self.cur_row)
        self.cur_row = [self._NONE]*self.num_cols

    def get_largest_component_size(self):
        return sorted(self.component_size.values(),reverse=True)[0]

    #since we move from left to right and top to bottom (i.e. no random access)
    # we only have to get maximum of 4 components: the three in the previous
    # row and the neighbor to the left in the current row:
    #                         A B C
    #                         D X
    def get_bordering_components(self,ndx):
        ids = set()
                
        if(ndx != self.num_cols-1):
            ids.add(self.prev_row[ndx+1])
        
        if(ndx != 0):
            ids.add(self.prev_row[ndx-1])
            ids.add(self.cur_row[ndx-1])
        
        ids.add(self.prev_row[ndx])
        
        return ids.difference({self._NONE})


    def merge_components(self, new_id, merge_id, ndx):
        for i in range(self.num_cols):
            if self.prev_row[i] == merge_id:
                self.prev_row[i] = new_id

        for i in range(ndx):
            if self.cur_row[i] == merge_id:
                self.cur_row[i] = new_id
                
        assert(new_id in self.component_size)
        assert(merge_id in self.component_size)
        self.component_size[new_id] += self.component_size[merge_id]

        #not strictly necessary, since the merged size will always be larger,
        # but better to keep the data structure clean        
        del self.component_size[merge_id]   


    def update_components(self,ndx):
        #component ids which border this cell
        ids = self.get_bordering_components(ndx);
        
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
                self.merge_components(this_id,merge_id,ndx)


def read_int():
    x = None
    while not x:
        try:
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'
    return x

def read_row(num_cols):
    row = []
    s = raw_input()
    
    num_strs = s.strip().split()
    assert(len(num_strs) == num_cols)
    
    for i in range(num_cols):
        row.append(int(num_strs[i]))
    
    assert(len(row) == num_cols)
    return row


#read number of rows and columns
m = read_int()
n = read_int()

#create an instance of the component tracker to solve the problem                
tracker = component_tracker(n)

for i_row in range(m):
    row = read_row(n)
    tracker.process_row(row)

#print tracker.component_size
print tracker.get_largest_component_size()


