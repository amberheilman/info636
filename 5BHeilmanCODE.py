"""
Name: Assignment 4B

Purpose:
- Read out one entry at a time from a file ( ie. 4.2, 75, 78, 96.4, 382 )
- User may (A) Accept (R) Replace (I) Insert or (D) Delete the entry shown
- User may (S) Save file with remainder of entries unchanged
- User may (W) Rename file and leave original file undisturbed
Error Conditions:
-Reach end of file
-Improper mode selection -> repeat mode selection
-Improper data entry -> repeat data entry
-Improper formatted file name/address -> repeat file  entry
-User enters existing file when creating new file -> repeat file entry
-User enters non-existing file when read/modifying -> repeat file entry

Assumption: 
-The file you are attempting to use is not empty
-K is set within the program code
-Entries must be real numbers separated by a ", "
 for each number in the array
"""

class File:

    """Global Variables"""
    def __init__ (self):

        self.temp_file = None
        self.filename = None
        self.index = 0
        self.k = 10

    """
    Function prompt(): opens file and saves contents to temp_file variable
    Return: void
    Parameters: None
    """
    def prompt(self):

        while self.temp_file is None:

            try:
                #open file for read
                file = open(self.filename, "r+")

                #save an array to keep track of changes
                self.temp_file = file.readlines()
                
                file.close()
                self.display()

            except (TypeError, IOError):
                self.filename = raw_input("What is the file name (ie /home/filename.txt) ? ")
                
    """
    Function display(): keeps track of entry within the temp_file
                        controller that executes mode
    Return: void
    Parameters: None
    """
    def display(self):

        while self.index < len(self.temp_file):

            #print the number
            print "Here is your entry  %s" % (self.temp_file[self.index])

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

            try:
                self.temp_file[self.index]
            except:
                self.destroy(self.filename)

    """
    Function replace(): changes the entry to new entry specified
    Return: void
    Parameters: None
    """
    def replace(self):
        #replaces temp array
        new_num = raw_input("What is the new entry ie '12.45, 23.45' ? ")
        try:
            new_num = tuple( float(i) for i in new_num.split(',') )
            while len(new_num) > self.k: raise Exception("Array larger than K")
            self.temp_file[self.index] = new_num
        except Exception, e:
            print e
            self.error()
            self.replace()

    """
    Function insert(): adds an entry to the next index of temp_file
    Return: void
    Parameters: None
    """
    def insert(self):
        new_num = raw_input("What is the new entry ie '12.45, 23.45' ? ")
        try:
            new_num = tuple( float(i) for i in new_num.split(',') )
            while len(new_num) > self.k: raise Exception("Array larger than K")
            self.temp_file[self.index+1] = new_num
        except Exception, e:
            print e
            if not type(new_num) == tuple:
                self.error()
                self.insert()
            if not self.temp_file[self.index+1]:
                self.error()
                self.insert()
            else:
                self.temp_file.append(new_num)

    """
    Function delete(): removes entry of temp_file
    Return: void
    Parameters: None
    """
    def delete(self):
        try:
            del self.temp_file[self.index]
        except:
            self.destroy(self.filename)
            

    """
    Function write(): retrieves file name to save temp_file array to
                      calls destroy() to save file
    Return: void
    Parameters: None
    """
    def write(self):
        new_filename = raw_input("New file name (ie file.py): ")
        try:
            if open(new_filename).readlines():
                self.error()
                self.write()
        except:
            self.destroy(new_filename)

    """
    Function error(): outputs a message to command line
    Return: void
    Parameters: None
    """
    def error(self):
        print "Incorrect Entry. Please try again!"

    """
    Function destroy(): saves the temp_file array to filename specified
    Return: void
    Parameters: file_name -> string
    """
    def destroy(self, file_name):
        try:
            file = open(file_name, "w")
            for num in self.temp_file:
                file.write(str(num).strip()+ "\n")
        except Exception, e:
            self.error()
            self.write()
        
        file.close()

file = File()
file.prompt()
