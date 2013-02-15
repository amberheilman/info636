'''
Name: Assignment 1B

Purpose: This program will use the command line to
either read or write real numbers to a user specified file

Version: 1.0
'''


'''
Main function prompt()

    Return: void
    Parameters: none
    Notes: uses command line raw_input
'''

def prompt():
    #prompt user to enter file name
    filename = raw_input("What is the file name (ie /home/filename.txt) ? ")

    #open file for read or write
    filename = open(filename, "ab+")

    #ask user to read or write
    mode = raw_input("Choose mode. Please type r to read, w for write: ")

    #user read mode
    if mode == "r":
        print(filename.read())
    
    #user write mode, appends if existing file
    if mode == "w":
        count = int(raw_input("How many numbers would you like to add? "))
        while(count > 0):
            #provide user with entry number
            input = raw_input("Enter number %s: "%count)
            filename.write(input + '\n')
            count= count-1
	    
    #close file
    filename.close() 

#run the program
prompt()
