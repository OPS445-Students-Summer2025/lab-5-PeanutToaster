#!/usr/bin/env python3
# Author ID: rtang41

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') #open function for data.txt to enable reading contents
    fread = f.read()
    f.close()
    return fread #returns whole content as string

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    # f = open(file_name, 'r')
    # words = [] #new list to append stripped words
    # fread = f.readlines() #variable to store lines of words
    # f.close()
    # for word in fread: #for loop to strip and append to words list
    #     words.append(word.strip())
    # return words #return list of stripped words

    #read the file into fread variable for memory, and close it
    f = open(file_name, 'r')
    fread = f.read()
    f.close()
    #make a list out of the contents of the file
    flist = fread.split('\n')
    length = len(flist)

    #splice last character of each item in list and return result
    splicelast = flist[0:length-1]
    return splicelast

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a') #opens file_name argument with 'a' to append
    f.write(str(string_of_lines)) #converts argument to string before appending
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w') #'w' for writing to file
    for l in list_of_lines:
        f.write(l + '\n')  #for loop for writing separate lines
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    #two arguments -> filepaths
    #read data from first argument to be written into second argument
    #line numbers to BEGINNING of each line with colon; for loop to count?
    # sample:
    # 1:Line 1
    # 2:Line 2
    # 3:Line 3

    paste = read_file_list(file_name_read) #read file for contents to paste using earlier function
    f = open(file_name_write, 'w') #start by clearing write file

    f = open(file_name_write, 'a') #append write file
    c = 1 # count variable starting at 1 for each line
    for line in paste: #for loop using read file
        f.write(str(c) + ":" + line + '\n') #write line # as c followed by
        c = c + 1 #+1 for each line
    f.close() #close when for loop ends

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))