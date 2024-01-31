@7   //{'code': ['push', 'constant', '7'], 'file': 'SimpleAdd', 'num': '6'}
D=A
@SP
M=M+1
A=M-1
M=D
@8   //{'code': ['push', 'constant', '8'], 'file': 'SimpleAdd', 'num': '7'}
D=A
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