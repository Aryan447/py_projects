'''
0 3 4 2
YES
'''

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the previous character
        else:
            stack.append(char)  # Add current character
    return ''.join(stack) if stack else "Empty String"

string = "aab"

print(superReducedString(string))
