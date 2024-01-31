@3030   //{'code': ['push', 'constant', '3030'], 'file': 'PointerTest', 'num': '7'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '0'], 'file': 'PointerTest', 'num': '8'}
M=M-1
A=M
D=M
@THIS
M=D
@3040   //{'code': ['push', 'constant', '3040'], 'file': 'PointerTest', 'num': '9'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'PointerTest', 'num': '10'}
M=M-1
A=M
D=M
@THAT
M=D
@32   //{'code': ['push', 'constant', '32'], 'file': 'PointerTest', 'num': '11'}
D=A
@SP
M=M+1
A=M-1
M=D
@THIS   //{'code': ['pop', 'this', '2'], 'file': 'PointerTest', 'num': '12'}
D=M
@2
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
@46   //{'code': ['push', 'constant', '46'], 'file': 'PointerTest', 'num': '13'}
D=A
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['pop', 'that', '6'], 'file': 'PointerTest', 'num': '14'}
D=M
@6
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
@THIS   //{'code': ['push', 'pointer', '0'], 'file': 'PointerTest', 'num': '15'}
D=M
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['push', 'pointer', '1'], 'file': 'PointerTest', 'num': '16'}
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
@THIS   //{'code': ['push', 'this', '2'], 'file': 'PointerTest', 'num': '18'}
D=M
@2
A=D+A
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
@THAT   //{'code': ['push', 'that', '6'], 'file': 'PointerTest', 'num': '20'}
D=M
@6
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