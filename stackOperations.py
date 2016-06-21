def drop(stack):
    stack.pop()
    return stack

def dup(stack):
    stack.append(stack[-1])
    return stack

def pop(stack):
    a = stack.pop()
    return (a, stack)

def popa(memory, stack):
    address = stack.pop()
    value = stack.pop()
    memory[address] = value
    return (memory,stack)

def pull(memory, stack):
    address = stack.pop()
    stack.append(memory[address])
    return (memory,stack)

def push(stack, instruction):
    value = int(instruction[1])
    stack.append(value)
    return stack

def pusha(stack):
    pass
    
def rot(stack):
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    stack.append(a)
    stack.append(b)
    stack.append(c)
    return stack

def swap(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)
    return stack
