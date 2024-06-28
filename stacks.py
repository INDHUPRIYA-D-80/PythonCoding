def balanced_parentheses(exp):
    stack = []
    
    for char in exp:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:   #Stack is empty
                return False
    if len(stack) > 0:
        return False
    return True

expression ="((()())"
print(balanced_parentheses(expression))