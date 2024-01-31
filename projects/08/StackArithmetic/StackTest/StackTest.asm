@17   //{'code': ['push', 'constant', '17'], 'file': 'StackTest', 'num': '7'}
D=A
@SP
M=M+1
A=M-1
M=D
@17   //{'code': ['push', 'constant', '17'], 'file': 'StackTest', 'num': '8'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['eq'], 'file': 'StackTest', 'num': '9'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISeq9
D;JEQ
@SP
A=M-1
M=0
@SKIPeq9
0;JMP
(ISeq9)
@SP
A=M-1
M=-1
(SKIPeq9)
@17   //{'code': ['push', 'constant', '17'], 'file': 'StackTest', 'num': '10'}
D=A
@SP
M=M+1
A=M-1
M=D
@16   //{'code': ['push', 'constant', '16'], 'file': 'StackTest', 'num': '11'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['eq'], 'file': 'StackTest', 'num': '12'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISeq12
D;JEQ
@SP
A=M-1
M=0
@SKIPeq12
0;JMP
(ISeq12)
@SP
A=M-1
M=-1
(SKIPeq12)
@16   //{'code': ['push', 'constant', '16'], 'file': 'StackTest', 'num': '13'}
D=A
@SP
M=M+1
A=M-1
M=D
@17   //{'code': ['push', 'constant', '17'], 'file': 'StackTest', 'num': '14'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['eq'], 'file': 'StackTest', 'num': '15'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISeq15
D;JEQ
@SP
A=M-1
M=0
@SKIPeq15
0;JMP
(ISeq15)
@SP
A=M-1
M=-1
(SKIPeq15)
@892   //{'code': ['push', 'constant', '892'], 'file': 'StackTest', 'num': '16'}
D=A
@SP
M=M+1
A=M-1
M=D
@891   //{'code': ['push', 'constant', '891'], 'file': 'StackTest', 'num': '17'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['lt'], 'file': 'StackTest', 'num': '18'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISlt18
D;JLT
@SP
A=M-1
M=0
@SKIPlt18
0;JMP
(ISlt18)
@SP
A=M-1
M=-1
(SKIPlt18)
@891   //{'code': ['push', 'constant', '891'], 'file': 'StackTest', 'num': '19'}
D=A
@SP
M=M+1
A=M-1
M=D
@892   //{'code': ['push', 'constant', '892'], 'file': 'StackTest', 'num': '20'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['lt'], 'file': 'StackTest', 'num': '21'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISlt21
D;JLT
@SP
A=M-1
M=0
@SKIPlt21
0;JMP
(ISlt21)
@SP
A=M-1
M=-1
(SKIPlt21)
@891   //{'code': ['push', 'constant', '891'], 'file': 'StackTest', 'num': '22'}
D=A
@SP
M=M+1
A=M-1
M=D
@891   //{'code': ['push', 'constant', '891'], 'file': 'StackTest', 'num': '23'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['lt'], 'file': 'StackTest', 'num': '24'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISlt24
D;JLT
@SP
A=M-1
M=0
@SKIPlt24
0;JMP
(ISlt24)
@SP
A=M-1
M=-1
(SKIPlt24)
@32767   //{'code': ['push', 'constant', '32767'], 'file': 'StackTest', 'num': '25'}
D=A
@SP
M=M+1
A=M-1
M=D
@32766   //{'code': ['push', 'constant', '32766'], 'file': 'StackTest', 'num': '26'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['gt'], 'file': 'StackTest', 'num': '27'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISgt27
D;JGT
@SP
A=M-1
M=0
@SKIPgt27
0;JMP
(ISgt27)
@SP
A=M-1
M=-1
(SKIPgt27)
@32766   //{'code': ['push', 'constant', '32766'], 'file': 'StackTest', 'num': '28'}
D=A
@SP
M=M+1
A=M-1
M=D
@32767   //{'code': ['push', 'constant', '32767'], 'file': 'StackTest', 'num': '29'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['gt'], 'file': 'StackTest', 'num': '30'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISgt30
D;JGT
@SP
A=M-1
M=0
@SKIPgt30
0;JMP
(ISgt30)
@SP
A=M-1
M=-1
(SKIPgt30)
@32766   //{'code': ['push', 'constant', '32766'], 'file': 'StackTest', 'num': '31'}
D=A
@SP
M=M+1
A=M-1
M=D
@32766   //{'code': ['push', 'constant', '32766'], 'file': 'StackTest', 'num': '32'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['gt'], 'file': 'StackTest', 'num': '33'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISgt33
D;JGT
@SP
A=M-1
M=0
@SKIPgt33
0;JMP
(ISgt33)
@SP
A=M-1
M=-1
(SKIPgt33)
@57   //{'code': ['push', 'constant', '57'], 'file': 'StackTest', 'num': '34'}
D=A
@SP
M=M+1
A=M-1
M=D
@31   //{'code': ['push', 'constant', '31'], 'file': 'StackTest', 'num': '35'}
D=A
@SP
M=M+1
A=M-1
M=D
@53   //{'code': ['push', 'constant', '53'], 'file': 'StackTest', 'num': '36'}
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
@112   //{'code': ['push', 'constant', '112'], 'file': 'StackTest', 'num': '38'}
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
@SP  //{op}
A=M-1
M=-M
@SP  //and
M=M-1
A=M
D=M
@SP
A=M-1
M=D&M
@82   //{'code': ['push', 'constant', '82'], 'file': 'StackTest', 'num': '42'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //or
M=M-1
A=M
D=M
@SP
A=M-1
M=D|M
@SP  //{op}
A=M-1
M=!M