

def add(result, instruction, getters, setters): 
    result.append('//add')
    prepTwoValueArithmetic(result)
    result.append('M=D+M')
    
def neg(result, instruction, getters, setters):
    result.append('//neg: ' + ' '.join(instruction))
    prepOneValueArithmetic(result)
    result.append('M=-D')

def sub(result, instruction, getters, setters):
    result.append('//sub: ' + ' '.join(instruction))
    prepTwoValueArithmetic(result)
    result.append('M=M-D')

def prepTwoValueArithmetic(result):
    result.append('@SP')
    result.append('M=M-1')
    result.append('A=M')
    result.append('D=M')
    result.append('A=A-1')
    
def prepOneValueArithmetic(result):
    result.append('@SP')
    result.append('D=M-1')
    result.append('A=D')
    result.append('D=M')