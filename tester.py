"""
1. read the document.
2. retrieve it line by line.
3. remove spaces
4. remove any characters != open or closed brackets.
5. if p is an open bracket of any kind, append to stack.
6. if p is a closed bracket, get the index of p in closed bracket list, and pop out that index of open bracket list from stack
7. exceptexcept IndexError:  # too many closing parens
                return False
8. return length of the stack == 0
"""
opening = ["(", "{", "[", "<", "(*"]
closing = [")", "}", "]", ">", "*)"]

def is_nested(line):
    i = 0
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
                return "No"
                break
        i += 1
        
        
    
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"
print(is_nested("<(************)>"))