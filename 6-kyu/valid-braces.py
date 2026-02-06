def valid_braces(string): # classic stack
    valid_braces = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for ch in string:
        if ch in valid_braces:
            if len(stack) != 0 and stack[-1] == valid_braces[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return True if len(stack) == 0 else False
    
print(valid_braces("(((({{"))