postfix = "512+4*+3-"
stack = []
for val in postfix:
    if val not in ['+','-','*','/']:
        stack.append(val)
    else:
        y = stack.pop()
        x = stack.pop()
        if (x=='0' or y=='0') and val == '/':
            stack.append(str(0))
        else:
            stack.append(str(eval(x+val+y)))
print stack[0]
