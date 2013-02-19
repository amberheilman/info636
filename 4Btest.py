"""
Name: Assignment 4B

Purpose:
- read out one number at a time from a file
- User may (A) Accept (R) Replace (I) Insert or (D) Delete the number shown
- User may (S) Save file with remainder of numbers unchanged
- User may (W) Rename file and leave original file undisturbed
Error Conditions:
-Reach end of file
-Improper mode selection -> repeat mode selection
-Improper data entry -> repeat data entry
-Improper formatted file name/address -> repeat file  entry
-User enters existing file when creating new file -> repeat file entry
-User enters non-existing file when read/modifying -> repeat file entry

"""
import sys

class File:


    def __init__ (self):

        self.temp_file = []
        self.filename = None
        self.index = 0

    def prompt(self):

        while self.temp_file is None:

            #prompt user to enter file name
            
            filename = raw_input("What is the file name (ie /home/filename.txt) ? ")

            #open file for read
            file = open(filename, "r+")

            #save an array to keep track of changes
            self.temp_file = file.readlines()

            file.close()
            display()

    def display(self):

        while self.index < len(self.temp_file):

            #print the number
            print "Here is your number  %s" % (self.temp_file[index])

            #prompt user for mode
            mode = raw_input("What would you like to do? Type (A)Accept (R) Replace (I) Insert (D) Delete (S) Save (W) Write new File: ")

            if mode == "R":
                replace(index)

            if mode == "I":
                insert()

            if mode == "D":
                delete(self.index)

            if mode == "A":
                pass

            if mode == "S":
                destroy(self.file)
                break

            if mode == "W":
                write()
                break

            elif mode not in ["A", "R", "I", "D", "S", "W"]:
                self.index = self.index-1
                error()
            self.index = self.index + 1

    def replace(self, index):
        #replaces temp array
        new_num = raw_input("What is the new number? ")
        if check_data(new_num):
            self.temp_file[index] = new_num + "\n"
        else:
            pass

    def insert(self):

        #inserts to temp array
        new_num = raw_input("What is the new number? ")
        if check_data(new_num):
            try:
                self.temp_file[index+1] = new_num + "\n"
            except:
                selftemp_file.append(new_num + "\n")
        else:
            pass
    
    def delete(self, index):
        #delete removes from global temp array
        del self.temp_file[index]
    
    def write(self):
        #if mode is (W) Write, then prompt and save and quit
        new_filename = raw_input("New file name (ie file.py): ")
        try:
            open(new_filename, "r")
            error()
            write()
        except:
            destroy(new_filename)
    
    def error(self):
        print "Incorrect Entry. Please try again!"
    
    def check_data(self, num):
        try:
            num = int(num)
        except:
            error()
    
    def destroy(self, file_name):
        try:
            file = open(file_name, "w")
            for num in self.temp_file:
                print num
                file.write(num)
            file.close()
        except:
            error()
            write()

    if __name__ == "main":
        prompt()
file = File()
file.main()
print "saldfkjsdalf"
