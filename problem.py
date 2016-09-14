# -*- coding: utf-8 -*-
"""

@author: Tom Dodson

Python 2.7
Created on Wed Sep 14 14:24:29 2016

"""
#Class that uses breadth-first search to solve for the largest connected component
# in a matrix. Constructor must be called with arguments of number of rows and
# columns.
#
#The class has two public methods:
# -update_cells_from_row() sets up the necessary data structures per row
# -get_largest_component_size() solves the instance (if it's unsolved) and 
#  returns the size of the largest connected component
#
#The matrix is represented internally by sets of tuples representing (row,col), 
# i.e. the matrix
#            1 1 1 0
#            1 0 0 0
#            0 0 1 0
#            0 0 0 1
# would have occupied_sites={(0,0),(0,1),(0,2),(1,0),(2,2),(3,3)}. It would 
# perform BFS starting at (0,0), finding the component of size 4. Then, since (2,2)
# was unvisited during the first search, BFS would be started again from (2,2),
# finding the component of size 2.
#
class BFS_solver:
    def __init__(self,m,n):
        self.num_rows = m
        self.num_cols = n
        self.component_sizes = []
        
        #these are sets of coordinate tuples that represent cells in the matrix
        self.occupied_sites = set()
        self.discovered_sites = set()

    #add the occupied sites in this row to the set of occupied sites
    def update_cells_from_row(self, row, i_row):
        assert(self.num_cols == len(row))
        
        for i_col in range(self.num_cols):
            if row[i_col]:
                self.occupied_sites.add((i_row,i_col))

    #start breadth-first search at the site t=(row,col)
    def __breadth_first_search(self,t):
        assert(t in self.occupied_sites and t not in self.discovered_sites)
        
        #initialize the search - we have visited no sites, so size is zero,
        # but we've discovered the first occupied site, t
        size = 0
        queue = [t]
        self.discovered_sites.add(t)
        
        #while we still have discovered sites to visit...
        while len(queue):
            #visit the site
            r,c = queue.pop()
            size += 1

            #check the neighbors for occupied, undiscovered sites
            neighbors = [(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]
            for t in neighbors:
                if t in self.occupied_sites and t not in self.discovered_sites:
                    queue.append(t)
                    self.discovered_sites.add(t)
        
        #no more neighbors to visit, so we've measured the size of the component
        self.component_sizes.append(size)
        
    def __solve_instance(self):
        #iterate through the whole instance, starting a breadth-first search 
        # whenever an unvisited site is encountered
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                t = (i,j)
                if t in self.occupied_sites and t not in self.discovered_sites:
                    self.__breadth_first_search(t)
    
    #lazily evaluates the component sizes, then returns the largest size
    def get_largest_component_size(self):
        if(len(self.component_sizes) == 0):
            self.__solve_instance()
        
        return sorted(self.component_sizes,reverse=True)[0]


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

#create the solver
solver = BFS_solver(m,n)

#read each row of the matrix, then add the row to the solver
for i_row in range(m):
    row = read_row()
    assert(len(row) == n)
    
    solver.update_cells_from_row(row,i_row)

print solver.get_largest_component_size()
