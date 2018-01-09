#!/bin/python

filename = raw_input("File name: ")
line_number = raw_input("Line number: ")

try:
    f = open(filename, "r")
    lines = f.readlines()
    try:
        line_number = int(line_number)
        print(lines[line_number])
    except ValueError:
        print('Line number value not an int')
    except IndexError:
        print('File is to short')
except IOError:
    print('File not found')

