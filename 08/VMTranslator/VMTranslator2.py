import sys
from LogicalOperations import *
from MemoryLocationManagement import *
from MathOperations import *
from StackArithmetic import *

fileToParse = sys.argv[1]
resultFile = sys.argv[2]

def getCode(file_name):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    code = []
    for line in lines:
        line = line.strip('\r\n').split('/')[0]
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

def label(result, instruction, getters, setters):
    result.append('//label ' + instruction[1])
    result.append('('+instruction[1]+')')
    
def ifGoto(result, instruction, getters, setters):
    result.append('//if-goto ' + instruction[1])
    result.append('@SP')
    result.append('M=M-1')
    result.append('A=M')
    result.append('D=M')
    result.append('@'+instruction[1])
    result.append('D;JNE')
    
def goto(result, instruction, getters, setters):
    result.append('@'+instruction[1])
    result.append('D;JMP')

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
    'not': notParser,
    'label': label,
    'if-goto': ifGoto,
    'goto': goto
}


code = getCode(fileToParse)
result = parseCode(code, parsers, getters, setters)
writeToFile(result)






