#!/bin/python

file_name = raw_input()
with open(file_name, "w") as f:
    line = raw_input();
    while line:
        f.write(line+"\n")
        line = raw_input()
