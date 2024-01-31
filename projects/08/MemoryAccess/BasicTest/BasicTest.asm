@10   //{'code': ['push', 'constant', '10'], 'file': 'BasicTest', 'num': '0'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['pop', 'local', '0'], 'file': 'BasicTest', 'num': '1'}
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
@21   //{'code': ['push', 'constant', '21'], 'file': 'BasicTest', 'num': '2'}
D=A
@SP
M=M+1
A=M-1
M=D
@22   //{'code': ['push', 'constant', '22'], 'file': 'BasicTest', 'num': '3'}
D=A
@SP
M=M+1
A=M-1
M=D
@ARG   //{'code': ['pop', 'argument', '2'], 'file': 'BasicTest', 'num': '4'}
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
@ARG   //{'code': ['pop', 'argument', '1'], 'file': 'BasicTest', 'num': '5'}
D=M
@1
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
@36   //{'code': ['push', 'constant', '36'], 'file': 'BasicTest', 'num': '6'}
D=A
@SP
M=M+1
A=M-1
M=D
@THIS   //{'code': ['pop', 'this', '6'], 'file': 'BasicTest', 'num': '7'}
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
@42   //{'code': ['push', 'constant', '42'], 'file': 'BasicTest', 'num': '8'}
D=A
@SP
M=M+1
A=M-1
M=D
@45   //{'code': ['push', 'constant', '45'], 'file': 'BasicTest', 'num': '9'}
D=A
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['pop', 'that', '5'], 'file': 'BasicTest', 'num': '10'}
D=M
@5
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
@THAT   //{'code': ['pop', 'that', '2'], 'file': 'BasicTest', 'num': '11'}
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
@510   //{'code': ['push', 'constant', '510'], 'file': 'BasicTest', 'num': '12'}
D=A
@SP
M=M+1
A=M-1
M=D
@5   //{'code': ['pop', 'temp', '6'], 'file': 'BasicTest', 'num': '13'}
D=A
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
@LCL   //{'code': ['push', 'local', '0'], 'file': 'BasicTest', 'num': '14'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['push', 'that', '5'], 'file': 'BasicTest', 'num': '15'}
D=M
@5
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
@ARG   //{'code': ['push', 'argument', '1'], 'file': 'BasicTest', 'num': '17'}
D=M
@1
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
@THIS   //{'code': ['push', 'this', '6'], 'file': 'BasicTest', 'num': '19'}
D=M
@6
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@THIS   //{'code': ['push', 'this', '6'], 'file': 'BasicTest', 'num': '20'}
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
@SP  //sub
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
@5   //{'code': ['push', 'temp', '6'], 'file': 'BasicTest', 'num': '23'}
D=A
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