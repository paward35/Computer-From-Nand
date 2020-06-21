
iid = 1
def next_id():
    global iid
    res = iid
    iid += 1
    return str(res)

def perpLogicalOperation(result, opp):
    id = next_id()
    result.append('D=M-D')
    result.append('@TRUE' + id)
    result.append('D;J'+opp)
    result.append('@SP')
    result.append('M=M-1')
    result.append('A=M')
    result.append('M=0')
    result.append('@FALSE' + id)
    result.append('0;JMP')
    result.append('(TRUE'+id+')')
    result.append('@SP')
    result.append('M=M-1')
    result.append('A=M')
    result.append('M=-1')
    result.append('(FALSE'+id+')')
    result.append('@SP')
    result.append('M=M+1')
    
def eq(result, instruction, getters, setters):
    result.append('//eq')
    prepTwoValueArithmetic(result)
    perpLogicalOperation(result, 'EQ')
    

def lt(result, instruction, getters, setters):
    result.append('//lt')
    prepTwoValueArithmetic(result)
    perpLogicalOperation(result, 'LT')

def gt(result, instruction, getters, setters):
    result.append('//gt')
    prepTwoValueArithmetic(result)
    perpLogicalOperation(result, 'GT')
    
def andParser(result, instruction, getters, setters):
    result.append('//and: ' + ' '.join(instruction))
    prepTwoValueArithmetic(result)
    result.append('M=D&M')
    
def orParser(result, instruction, getters, setters):
    result.append('//or: ' + ' '.join(instruction))
    prepTwoValueArithmetic(result)
    result.append('M=D|M')
    
def notParser(result, instruction, getters, setters):
    result.append('//not: ' + ' '.join(instruction))
    prepOneValueArithmetic(result)
    result.append('M=!D')