
import sys

fileToParse = sys.argv[1]
resultFile = sys.argv[2]
variableCounter = 16
symbols = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4
}

print(symbols)
#load files 
def getCode(file_name):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    code = []
    for line in lines:
        line = line.strip('\r\n').replace(" ", "")
        if(len(line) != 0 and line[0] != '/'):
            if(line.startswith('(')):
                line = line.replace("(", "").replace(")", "")
                symbols[line] = len(code)
            else:
                code.append(line.split('/', 1)[0])
    return code

code = getCode(fileToParse)
print(symbols)

def parseSymbol(instruction, variableCounter):
    print('')
    print(instruction)
    try:
        instruction = int(instruction)
    except:
        if symbols.get(instruction) == None:
            symbols[instruction] = variableCounter
            variableCounter = variableCounter + 1
        instruction = symbols[instruction]
    print(instruction)
    return [instruction, variableCounter]

def parseAInstruction(code, variableCounter):
    instruction = code[1:]
    [intRepresentation, variableCounter] = parseSymbol(instruction, variableCounter)
    binarRepresentation = str(bin(intRepresentation))[2:]
    binarRepresentationWithLeadingZeros = binarRepresentation.zfill(16)
    return [binarRepresentationWithLeadingZeros, variableCounter]

def parseDest(instruction):
    binaryRepresentation = ['0','0','0']
    if(instruction.find('M') != -1):
        binaryRepresentation[2] = '1'
    if(instruction.find('D') != -1):
        binaryRepresentation[1] = '1'
    if(instruction.find('A') != -1):
        binaryRepresentation[0] = '1'
    return "".join(binaryRepresentation)
    
jumpInstructions = {
    '': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

def parseJmp(instruction):
    return jumpInstructions[instruction]
    
def parseComp(instruction):
    return compSymbolTable[instruction]
    
compSymbolTable = {
    '0':   '0101010',
    '1':   '0111111',
    '-1':  '0111010',
    'D':   '0001100',
    'A':   '0110000',
    'M':   '1110000',
    '!D':  '0001101',
    '!A':  '0110001',
    '!M':  '1110001',
    '-D':  '0001111',
    '-A':  '0110011',
    '-M':  '1110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'M+1': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'D+M': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'D&M': '1000000',
    'D|A': '0010101',
    'D|M': '1010101',
}

def parseCInstruction(code):
    dest = ''
    jmp = ''
    if(code.find('=') != -1):
        dest = code.split('=', 1)[0]
        code = code.split('=', 1)[1]
    if(code.find(';') != -1):
        jmp = code.split(';', 1)[1]
        code = code.split(';', 1)[0]
    destBinary = parseDest(dest)
    jmpBinary = parseJmp(jmp)
    compBinary = parseComp(code)
    cInstruction = '111' + compBinary + destBinary + jmpBinary
    return cInstruction

def convertCodeToBinary(code, variableCounter):
    result = []
    for line in code:
        if(line.startswith('@')):
            [instruction,variableCounter] = parseAInstruction(line, variableCounter)
            result.append(instruction)
        else: 
            result.append(parseCInstruction(line))
    return result 
    
def writeToFile(code):
    with open(resultFile, 'w') as f:
        for item in code:
            f.write("%s\n" % item)

writeToFile(convertCodeToBinary(code, variableCounter))



    