import arithmetic
import programFlow
import stackOperations

def data():
    pass

def runAsm(asm):
    '''Takes source as a list of instructions, executes instructions on stack'''
    pc = 0
    stack = []
    returnStack = []
    variable = 0
    memory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    functions = {}
    data = {}
    progLength = len(asm)
    functions['eof'] = progLength
    run = True

    operations = {'add': arithmetic.add, 'sub': arithmetic.sub, 'div':arithmetic.div,
            'mult': arithmetic.mult, 'and': arithmetic.and_func, 'band': arithmetic.band,
            'bnot': arithmetic.bnot, 'bor': arithmetic.bor, 'bxor': arithmetic.bxor,
            'mod': arithmetic.mod, 'not': arithmetic.not_func, 'or': arithmetic.or_func,
            'xor': arithmetic.xor, 'eq': programFlow.eq, 'ge': programFlow.ge,
            'gt': programFlow.gt, 'le': programFlow.le, 'lt': programFlow.lt, 'ne': programFlow.ne,
            'nop': programFlow.nop, 'call': programFlow.call, 'ret': programFlow.ret,
            'stop': programFlow.stop, 'jtrue': programFlow.jtrue, 'jfalse': programFlow.jfalse,
            'jmp': programFlow.jmp, 'end': programFlow.end, 'push': stackOperations.push,
            'pop': stackOperations.pop, 'drop': stackOperations.drop, 'dup': stackOperations.dup,
            'swap': stackOperations.swap, 'popa': stackOperations.popa, 'pull': stackOperations.pull,
            'rot': stackOperations.rot, 'data': data}

    for instruction in range(0, progLength):
        asm[instruction] = asm[instruction].split()
        current = asm[instruction]
        if len(current) != 0:
            op = current[0]
            if op not in operations:
                functions[op] = instruction

    if len(current) > 1:
        func = programFlow.end(current)
        pc = functions[func]

    #print(functions, pc)
        
    while pc < progLength:
        instruction = asm[pc]
        if len(instruction) != 0:
            op = instruction[0]
            print(instruction, pc, variable)
            
            if op == 'data':
                try:
                    data[instruction[2]] = int(instruction[1])
                except ValueError:
                    data[instruction[1]] = None
                pc += 1
            elif op in operations and len(instruction) != 0:
                if op == 'data':
                    try:
                        data[instruction[2]] = int(instruction[1])
                    except ValueError:
                        data[instruction[1]] = None
                    pc += 1
                elif op == 'pop':
                    var = instruction[1]
                    if  var in data:
                        data[var],stack = stackOperations.pop(stack)
                        print(data[var])
                    else:
                        variable,stack = stackOperations.pop(stack)
                    pc += 1
                elif len(instruction) > 1 and instruction[1] in data:
                    instruction[1] = data[instruction[1]]
                
                method = operations[op]

                if op in ['jtrue', 'jfalse']:
                    stack,func = method(stack, instruction)
                    pc = functions[func]
                elif op == 'jmp':
                    func = method(instruction)
                    pc = functions[func]
                elif op == 'call':
                    func = method(instruction)
                    returnStack.append(pc+1)
                    #print(returnStack)
                    pc = functions[func]
                elif op == 'ret':
                    pc,returnStack = method(returnStack)
                elif op == 'push':
                    stack = method(stack, instruction)
                    pc += 1
                elif op in ['popa', 'pull']:
                    memory,stack = method(memory, stack)
                    pc += 1
                    print(memory)
                elif op == 'stop':
                    func = method()
                    pc = functions[func]
                    print(pc)
                elif op == 'end':
                    if len(instruction) < 2 or pc == progLength-1:
                        pc += 1
                    else:
                        func = method(instruction)
                        pc = functions[func]
                else:
                    stack = method(stack)
                    pc += 1
            else:
                pc += 1

        else:
            pc += 1

        print(data)
        print(stack)
        input()

##    hi = []
##    for i in operations:
##        hi.append(i)
##    print(hi)
    print(data)
    return stack

def main():
    inputf = open('source2.txt')
    asm = [line.strip('\n').strip('\t') for line in inputf.readlines()]

    print(runAsm(asm))

main()

#if __name__ == '__main__':
#    main()
