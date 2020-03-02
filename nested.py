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
    stack = []
    unbalanced = False
    pos = 0
    while line:
        paren = line[0]
        if line[:2] == "(*" or line[:2] == "*)":
            paren = line[:2]
        pos += 1
        if paren in closing:
            index = closing.index(paren)
            match = opening[index]
            if stack.pop() != match:
                unbalanced = True
                break
        if paren in opening:
            stack.append(paren)

        line = line[len(paren):]
    if stack or unbalanced:
        return 'No ' + str(pos)
    return 'Yes'



def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as nfile:
            for line in file:
                read_output = is_nested(line)
                print(read_output)
                nfile.write(read_output + '\n')
    


if __name__ == '__main__':
    main(sys.argv[1:])
