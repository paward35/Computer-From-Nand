@111   //{'code': ['push', 'constant', '111'], 'file': 'StaticTest', 'num': '6'}
D=A
@SP
M=M+1
A=M-1
M=D
@333   //{'code': ['push', 'constant', '333'], 'file': 'StaticTest', 'num': '7'}
D=A
@SP
M=M+1
A=M-1
M=D
@888   //{'code': ['push', 'constant', '888'], 'file': 'StaticTest', 'num': '8'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'static', '8'], 'file': 'StaticTest', 'num': '9'}
M=M-1
A=M
D=M
@StaticTest.8
M=D
@SP  //{'code': ['pop', 'static', '3'], 'file': 'StaticTest', 'num': '10'}
M=M-1
A=M
D=M
@StaticTest.3
M=D
@SP  //{'code': ['pop', 'static', '1'], 'file': 'StaticTest', 'num': '11'}
M=M-1
A=M
D=M
@StaticTest.1
M=D
@StaticTest.3   //{'code': ['push', 'static', '3'], 'file': 'StaticTest', 'num': '12'}
D=M
@SP
M=M+1
A=M-1
M=D
@StaticTest.1   //{'code': ['push', 'static', '1'], 'file': 'StaticTest', 'num': '13'}
D=M
@SP
M=M+1
A=M-1
M=D
@SP  //sub
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
@StaticTest.8   //{'code': ['push', 'static', '8'], 'file': 'StaticTest', 'num': '15'}
D=M
@SP
M=M+1
A=M-1
M=D
@SP  //add
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M