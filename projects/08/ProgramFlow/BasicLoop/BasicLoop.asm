@0   //{'code': ['push', 'constant', '0'], 'file': 'BasicLoop', 'num': '9'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['pop', 'local', '0'], 'file': 'BasicLoop', 'num': '10'}
D=M
@0
D=D+A
@SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
(LOOP)   //{'code': ['label', 'LOOP'], 'file': 'BasicLoop', 'num': '11'}
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'BasicLoop', 'num': '12'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['push', 'local', '0'], 'file': 'BasicLoop', 'num': '13'}
D=M
@0
A=D+A
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
@LCL   //{'code': ['pop', 'local', '0'], 'file': 'BasicLoop', 'num': '15'}
D=M
@0
D=D+A
@SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'BasicLoop', 'num': '16'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@1   //{'code': ['push', 'constant', '1'], 'file': 'BasicLoop', 'num': '17'}
D=A
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
@ARG   //{'code': ['pop', 'argument', '0'], 'file': 'BasicLoop', 'num': '19'}
D=M
@0
D=D+A
@SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'BasicLoop', 'num': '20'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['if-goto', 'LOOP'], 'file': 'BasicLoop', 'num': '21'}
M=M-1
A=M
D=M
@LOOP
D;JNE
@LCL   //{'code': ['push', 'local', '0'], 'file': 'BasicLoop', 'num': '22'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D