
def push(result, instruction, getters, setters):
    result.append('//' + ' '.join(instruction))
    number = getters[instruction[1]](result, instruction[2])
    result.append('@SP')
    result.append('A=M')
    result.append('M=D')
    result.append('@SP')
    result.append('M=M+1')

def pop(result, instruction, getters, setters):
    result.append('//' + ' '.join(instruction))
    number = setters[instruction[1]](result, instruction[2])
    result.append('@SP')
    result.append('M=M-1')
    result.append('A=M')
    result.append('D=M')
    result.append('@R13')
    result.append('A=M')
    result.append('M=D')