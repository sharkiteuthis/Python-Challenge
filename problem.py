
# Python Challenge

# CLARIFICATION: Please keep in mind that we only have the time and
# resources to invite candidates for the in-person interview who send us a
# solution that produces the correct answer to the largest test case,
# the 1000x1000 grid, in 10 seconds or less.

# CLARIFICATION 2: Please keep in mind that while the above is the only
# "hard" requirement, we WILL be inspecting the actual written code in 
# depth to ascertain that it is of the excellent quality a position 
# on the Idea Evolver Engineering Team requires.

# CLARIFICATION 3:  I will run your solution with the 
# following at the OS X command line:
# `time python problem.py < hard-test-case1000x1000.txt`
# The symbol `<` that is the homophone of the mathematical "less than"
# sign is called the redirect operator.  If you are not familiar with 
# the unix/linux/os x command line or the redirect operator,
# this is something you need to google because we do not have
# the time or resources to explain it here.

# --------------------------------------

# Problem Description:

# You are given a matrix with m rows and n columns of cells, each of which
# contains either 1 or 0. Two cells are said to be connected if they are
# adjacent to each other horizontally, vertically, or diagonally. The connected
# and filled (i.e. cells that contain a 1) cells form a region. There may be
# several regions in the matrix. Find the number of cells in the largest region
# in the matrix.

# Input Format 
# There will be three parts of the input:
# The first line will contain m, the number of rows in the matrix.
# The second line will contain n, the number of columns in the matrix.
# This will be followed by the matrix grid: the list of numbers that make up the matrix.

# Output Format 
# Print the length of the largest region in the given matrix.

# Constraints
# 0<m<10
# 0<n<10

# Sample Input:
# 4
# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0

# Sample Output:
# 5

# Explanation
# X X 0 0
# 0 X X 0
# 0 0 X 0
# 1 0 0 0
# The X characters indicate the largest connected component, as per the given
# definition. There are five cells in this component.

# Task: 
# Write the complete program to find the number of cells in the largest region.

# You will need to read from stdin for the input and write to stdout for the output
# If you are unfamiliar with what that means:
# raw_input is a function that reads from stdin
# print statements write to stdout
# You are not required to use raw_input or print statements, but it is the
# simplest and most common way to read and write to stdin/out

# The test cases are located in the test-cases directory.
# ALL OF THE TEST CASES EXCEPT FOR THE 1000x1000 are just
# for you to test your solution on.  We will ONLY BE TESTING
# YOUR SOLUTION WITH THE 1000x1000 grid, `hard-test-case1000x1000.txt`.
# As stated at the top, we ONLY invite candidates who send us 
# a solution that produces the correct answer to the 1000x1000 grid
# in 10 seconds or less.

# run-tests.py is not part of your challenge.  It is simply a
# convenience program that will test your code against all the test
# cases (in the test-cases directory only, not the
# hard-test-case1000x1000.txt), one after another, and then tell you whether
# it passed or failed, and what the expected and actual outputs are.
# You may review and modify run-tests.py as much as you want, but it
# will not score or lose you any points

# You may generate test
# cases of various dimensions using generate-test-case.py, but the
# ability of your algorithm to solve extra test cases you've created
# will not be considered in our evaluation of this challenge.  THE
# ONLY HARD REQUIREMENT is the 1000x1000 in less than 10s.

# Finally, you may not use *third party* libraries to complete this
# challenge.  You may only use the libraries available on a fresh
# Python 2.7 install.  I doubt you will need to use any libraries at
# all as this is just an algorithmic challenge.  BUT YOU MAY USE
# ANYTHING FROM THE BUILT IN PYTHON STANDARD LIBRARY (e.g. functools,
# itertools, math, string, etc).  It is actually very impressive to
# see someone who is very comfortable with the entire python
# ecosystem.
