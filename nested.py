#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys

opening = ["(", "{", "[", "<", "(*"]
closing = [")", "}", "]", ">", "*)"]


def is_nested(line):
    i = 0
    err = 0
    stack = []
    stack2 = []
    while i < len(line):
        if line[i] in opening:
            stack.append(line[i])
        elif line[i] in closing:
            pos = closing.index(line[i])
            if ((len(stack) > 0) and (opening[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                with open('output.txt', 'a') as file:
                    file.writelines(" NO:" + str(err))
                    
                break
        i += 1
        err += 1
    if len(stack) == 0:
        with open('output.txt', 'a') as file:
            file.writelines(" YES ")
            
    else:
        with open('output.txt', 'a') as file:
            file.writelines(" NO:" + str(err))




def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt') as file:
        data = file.read()
        lines = data.split()
        
        for line in lines:
            is_nested(line)
    


if __name__ == '__main__':
    main(sys.argv[1:])
