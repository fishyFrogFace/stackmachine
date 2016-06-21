def add(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)
    return stack

def sub(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)
    return stack

def div(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)
    return stack

def mult(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)
    return stack

def and_func(stack):
    a = stack.pop()
    b = stack.pop()
    if a and b:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def band(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a&b)
    return stack

def bnot(stack):
    a = stack.pop()
    stack.append(~a)
    return stack

def bor(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a|b)
    return stack

def bxor(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a^b)
    return stack

def mod(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b%a)
    return stack

def not_func(stack):
    a = stack.pop()
    if not a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def or_func(stack):
    a = stack.pop()
    b = stack.pop()
    if a or b:
        stack.append(1)
    else:
        stack.append(0)
    pc += 1

def xor(stack):
    a = stack.pop()
    b = stack.pop()
    if bool(a) != bool(b):
        stack.append(1)
    else:
        stack.append(0)
