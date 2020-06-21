
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
    