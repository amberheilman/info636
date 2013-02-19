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

class File:


    def __init__ (self):

        self.temp_file = None
        self.filename = None
        self.index = 0
        

    def prompt(self):

        while self.temp_file is None:

            try:
                #open file for read
                file = open(self.filename, "r+")

                #save an array to keep track of changes
                self.temp_file = file.readlines()
                
                file.close()
                self.display()

            except:
                #prompt user to enter file name
                self.filename = raw_input("What is the file name (ie /home/filename.txt) ? ")
                


    def display(self):

        while self.index < len(self.temp_file):

            #print the number
            print "Here is your number  %s" % (self.temp_file[self.index])

            #prompt user for mode
            mode = raw_input("What would you like to do? Type (A)Accept (R) Replace (I) Insert (D) Delete (S) Save (W) Write new File: ")

            if mode == "R":
                self.replace()

            if mode == "I":
                self.insert()

            if mode == "D":
                self.delete()

            if mode == "A":
                pass

            if mode == "S":
                self.destroy(self.filename)
                break

            if mode == "W":
                self.write()
                break


            elif mode not in ["A", "R", "I", "D", "S", "W"]:
                self.index = self.index-1
                self.error()
            self.index = self.index + 1

    def replace(self):
        #replaces temp array
        new_num = raw_input("What is the new number? ")
        try:
            int(new_num)
            self.temp_file[self.index] = new_num + "\n"
        except:
            self.error()
            self.replace()
            
    def insert(self):

        #inserts to temp array
        new_num = raw_input("What is the new number? ")
        try:
            int(new_num)
            self.temp_file[self.index+1] = new_num + "\n"
        except:
            if not self.temp_file[self.index+1]:
                self.error()
                self.insert()
            else:
                self.temp_file.append(new_num + "\n")
                
    def delete(self):
        #delete removes from global temp array
        del self.temp_file[self.index]
    
    def write(self):
        #if mode is (W) Write, then prompt and save and quit
        new_filename = raw_input("New file name (ie file.py): ")
        try:
            open(new_filename, "r")
            self.error()
            self.write()
        except:
            self.destroy(new_filename)
    
    def error(self):
        print "Incorrect Entry. Please try again!"
    
    def destroy(self, file_name):
        try:
            file = open(file_name, "w")
            for num in self.temp_file:
                file.write(num)
        except:
            self.error()
            self.write()
        
        file.close()

file = File()
file.prompt()
