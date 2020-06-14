import sys

fileToParse = sys.argv[1]
resultFile = sys.argv[2]

iid = 1
def next_id():
    global iid
    res = iid
    iid += 1
    return str(res)

def getCode(file_name):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    code = []
    for line in lines:
        line = line.strip('\r\n')
        if(len(line) != 0 and line[0] != '/'):
            line = line.split(" ")
            code.append(line)
            
    return code

def writeToFile(code):
    with open(resultFile, 'w') as f:
        for item in code:
            f.write("%s\n" % item)
            
def parseCode(code, parsers, getters, setters):
    result = []
    for line in code:
        parsers[line[0]](result, line, getters, setters)
    return result

    
def add(result, instruction, getters, setters): 
    result.append('//add')
    prepTwoValueArithmetic(result)
    result.append('M=D+M')
    
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

def sub(result, instruction, getters, setters):
    result.append('//sub: ' + ' '.join(instruction))
    prepTwoValueArithmetic(result)
    result.append('M=M-D')
    
def neg(result, instruction, getters, setters):
    result.append('//neg: ' + ' '.join(instruction))
    prepOneValueArithmetic(result)
    result.append('M=-D')
    
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

def getConstant(result, number):
    result.append('@' + number)
    result.append('D=A')
    
def getStatic(result, number):
    result.append('@static'+number)
    result.append('D=M')
    
def setStatic(result, number):
    result.append('@static'+number)
    result.append('D=A')
    result.append('@R13')
    result.append('M=D')
    
def setArgument(result, number):
    result.append('@ARG')
    result.append('D=M')
    result.append('@' + number)
    result.append('D=A+D')
    result.append('@R13')
    result.append('M=D')

def getArgument(result, number):
    result.append('@ARG')
    result.append('D=M')
    result.append('@' + number)
    result.append('A=A+D')
    result.append('D=M')
    
    
def setLocal(result, number):
    result.append('@LCL')
    result.append('D=M')
    result.append('@' + number)
    result.append('D=A+D')
    result.append('@R13')
    result.append('M=D')

def getLocal(result, number):
    result.append('@LCL')
    result.append('D=M')
    result.append('@' + number)
    result.append('A=A+D')
    result.append('D=M')
    
def setThis(result, number):
    result.append('@THIS')
    result.append('D=M')
    result.append('@' + number)
    result.append('D=A+D')
    result.append('@R13')
    result.append('M=D')

def getThis(result, number):
    result.append('@THIS')
    result.append('D=M')
    result.append('@' + number)
    result.append('A=A+D')
    result.append('D=M')

def setThat(result, number):
    result.append('@THAT')
    result.append('D=M')
    result.append('@' + number)
    result.append('D=A+D')
    result.append('@R13')
    result.append('M=D')

def getThat(result, number):
    result.append('@THAT')
    result.append('D=M')
    result.append('@' + number)
    result.append('A=A+D')
    result.append('D=M')

def setTemp(result, number):
    number = int(number) + 5
    result.append('@' + str(number))
    result.append('D=A')
    result.append('@R13')
    result.append('M=D')

def getTemp(result, number):
    number = int(number) + 5
    result.append('@' + str(number))
    result.append('D=M')
    
def setPointer(result, number):
    if(number == '0'):
        result.append('@THIS')
    else:
        result.append('@THAT')
    result.append('D=A')
    result.append('@R13')
    result.append('M=D')

def getPointer(result, number):
    if(number == '0'):
        result.append('@THIS')
    else:
        result.append('@THAT')
    result.append('D=M')
    
def push(result, instruction, getters, setters):
    result.append('//' + ' '.join(instruction))
    number = getters[instruction[1]](result, instruction[2])
    result.append('@SP')
    result.append('A=M')
    result.append('M=D')
    result.append('@SP')
    result.append('M=M+1')

#Working here need address
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
    

    
getters = {
    'constant': getConstant,
    'static': getStatic,
    'argument': getArgument,
    'local': getLocal,
    'temp': getTemp,
    'this': getThis,
    'that': getThat,
    'pointer': getPointer
}

setters = {
    'static': setStatic,
    'argument': setArgument,
    'local': setLocal,
    'temp': setTemp,
    'this': setThis,
    'that': setThat,
    'pointer': setPointer,
}

parsers = {
    'pop': pop, 
    'push': push,
    'add': add,
    'eq': eq,
    'lt': lt,
    'gt': gt,
    'sub': sub,
    'neg': neg,
    'and': andParser,
    'or': orParser,
    'not': notParser
}

code = getCode(fileToParse)

result = parseCode(code, parsers, getters, setters)

writeToFile(result)

print(code)
print(result)





