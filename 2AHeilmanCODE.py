"""
Name: Assignment 2A

Purpose: This program will use the command line to
enter a file name and return logical lines of code

Version: 1.0
"""

"""
Main function prompt()

    Return: void
    Parameters: none
    Notes: prompts the user for file name and returns the LOC
"""
def prompt():

    #prompt user to enter file name
    filename = raw_input("What is the file name (ie /home/code.py) ? ")

    #call the external function to count lines in file
    num_of_lines = count_lines(filename)

    print num_of_lines

"""
Main function count_lines()

    Return: int
    Parameters: file name
    Notes: counts number of logical lines in a .py file
"""
def count_lines(filename):

    #line counter
    num_of_lines = 0

    #open file for read only
    filename = open(filename).readlines()

    #this will determine if we are in a docstring
    doc_string = False    

    for line in filename:

	line = line.strip()
	if line:	
            #do not count comments
            if line.startswith('#'):
	        continue
	
            #do not count docstrings
            if line.startswith('"""'):
	        doc_string = not doc_string
	        continue

            #count the number of logical lines
            if not doc_string:
		num_of_lines += 1

    return num_of_lines

prompt()
