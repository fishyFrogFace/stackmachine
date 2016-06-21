def call(instruction):
    func = instruction[1]
    return func

def end(instruction):
    func = instruction[1]
    return func

def eq(stack):
    a = stack.pop()
    b = stack.pop()
    if b == a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def ge(stack):
    a = stack.pop()
    b = stack.pop()
    if b >= a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def gt(stack):
    a = stack.pop()
    b = stack.pop()
    if b < a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def jfalse(stack, instruction):
    a = stack.pop()
    if not a:
        return stack
    func = instruction[1]
    return (stack, func)

def jmp(instruction):
    func = instruction[1]
    return func

def jtrue(stack, instruction):
    a = stack.pop()
    if a:
        func = instruction[1]
        return (stack, func)
    return stack

def le(stack):
    a = stack.pop()
    b = stack.pop()
    if b <= a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def lt(stack):
    a = stack.pop()
    b = stack.pop()
    if b > a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def ne(stack):
    a = stack.pop()
    b = stack.pop()
    if b != a:
        stack.append(1)
    else:
        stack.append(0)
    return stack

def nop(stack):
    return stack

def ret(returnStack):
    a = returnStack.pop()
    return (a, returnStack)

def stop():
    return 'eof'




