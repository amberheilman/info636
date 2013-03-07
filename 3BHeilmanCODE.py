"""
Name: Assignment 2B

Purpose:
- read out one number at a time from a file
- User may (A) Accept (R) Replace (I) Insert or (D) Delete the number shown
- User may (S) Save file with remainder of numbers unchanged
- User may (W) Rename file and leave original file undisturbed
Error Conditions:
-Reach end of file
-Improper mode selection -> repeat mode selection
-Improper data entry -> repeat data entry
"""

"""
Main function prompt()

Return: void
Parameters: none
Notes: Main function; uses command line raw_input
"""
def prompt():
    #prompt user to enter file name
    global filename
    filename = raw_input("What is the file name (ie /home/filename.txt) ? ")

    #open file for read
    global file
    file = open(filename, "r+") #above is old

    #save an array to keep track of changes
    global temp_file
    temp_file = file.readlines()

    file.close()
    display()

def display():
    global index
    index = 0

    while index < len(temp_file):

        #print the number
        print "Here is your number  %s" % (temp_file[index])

        #prompt user for mode
        mode = raw_input("What would you like to do? Type (A)Accept (R) Replace (I) Insert (D) Delete (S) Save (W) Write new File: ")

        if mode == "R":
            replace(index)

        if mode == "I":
            insert()

        if mode == "D":
            delete(index)

        if mode == "A":
            pass

        if mode == "S":
            destroy(file)
            break

        if mode == "W":
            write()
            break

        elif mode not in ["A", "R", "I", "D", "S", "W"]:
            index = index-1
            error()
        index = index + 1

def replace(index):
    #replaces temp array
    new_num = raw_input("What is the new number? ")
    if check_data(new_num):
        temp_file[index] = new_num + "\n"
    else:
        pass

def insert():
    #inserts to temp array
    new_num = raw_input("What is the new number? ")
    if check_data(new_num):
        try:
            temp_file[index+1] = new_num + "\n"
        except:
            temp_file.append(new_num + "\n")
    else:
        pass

def delete(index):
    #delete removes from global temp array
    del temp_file[index]

def write():
    #if mode is (W) Write, then prompt and save and quit
    new_filename = raw_input("New file name (ie file.py): ")
    destroy(new_file)

def error():
    print "Incorrect Entry.Please try again!"

def check_data(num):
    try:
        num = int(num)
    except:
        error()

def destroy(file_name):
    file = open(filename, "w")
    for num in temp_file:
        file.write(num)
    file.close() 

prompt()
