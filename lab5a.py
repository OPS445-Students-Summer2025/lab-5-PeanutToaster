#!/usr/bin/env python3
# Author ID: rtang41

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open('data.txt', 'r') #open function for data.txt to enable reading contents
    return f.read() #returns whole content as string

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    f = open('data.txt', 'r')
    words = [] #new list to append stripped words
    fread = f.readlines() #variable to store lines of words
    f.close()
    for word in fread: #for loop to strip and append to words list
        words.append(word.strip())
    return words #return list of stripped words

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))