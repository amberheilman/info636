"""
Name: Assignment 2B

Purpose:
- read out one number at a time from a file
- User may (A) Accept (R) Replace (I) Insert or (D) Delete the number shown
- User may (S) Save file with remainder of numbers unchanged
- User may (W) Rename file and leave original file undisturbed

"""

"""
Main function prompt()

    Return: void
    Parameters: none
    Notes: Main function; uses command line raw_input
"""
def prompt():

    #prompt user to enter file name
    filename = raw_input("What is the file name (ie /home/filename.txt) ? ")

    #open file for read or write
    file = open(filename, "r+")

    #save an array to keep track of changes
    temp_file = file.readlines()
    file.close()

    for index, num in enumerate(temp_file):
    #print the number
        print "Here is your number  %s" % (num.strip())

        #ask user to (A)Accept (R) Replace (I) Insert (D) Delete (S) Save (W) Write new File
        mode = raw_input("What would you like to do? Type (A)Accept (R) Replace (I) Insert (D) Delete (S) Save (W) Write new File: ") #mod

        #replaces in temp array
        if mode == "R":
            new_num = raw_input("What is the new number? ")
            temp_file[index] = new_num + "\n"

        #inserts to temp array
        if mode == "I":
            new_num = raw_input("What is the new number? ")
            try:
                temp_file[index+1] = new_num + "\n"
            except:
                temp_file.append(new_num + "\n")

        #delete removes from temp array
        if mode == "D":
            del temp_file[index]
            pass

        #if mode is (A) Accept, then pass
        if mode == "A":
            pass

        if index == len(temp_file):
            mode = raw_input("Reached the end of file (S) Save or (W) Write new File: ")

        #if mode is (S) Save, then save and quit
        if mode == "S":
            break

        #if mode is (W) Write, then prompt and save and quit
        if mode == "W":
            new_filename = raw_input("New file name (ie file.py): ")
            filename = new_filename
            new_file = open(new_filename, "w")
            break
        
    file = open(filename, "w+") 
    for num in temp_file:
        file.write(num)
    #close file
    file.close() 


prompt()

