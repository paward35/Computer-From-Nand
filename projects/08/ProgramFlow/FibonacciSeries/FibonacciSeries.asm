@ARG   //{'code': ['push', 'argument', '1'], 'file': 'FibonacciSeries', 'num': '9'}
D=M
@1
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'FibonacciSeries', 'num': '10'}
M=M-1
A=M
D=M
@THAT
M=D
@0   //{'code': ['push', 'constant', '0'], 'file': 'FibonacciSeries', 'num': '11'}
D=A
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['pop', 'that', '0'], 'file': 'FibonacciSeries', 'num': '12'}
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
@1   //{'code': ['push', 'constant', '1'], 'file': 'FibonacciSeries', 'num': '13'}
D=A
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['pop', 'that', '1'], 'file': 'FibonacciSeries', 'num': '14'}
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
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'FibonacciSeries', 'num': '15'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@2   //{'code': ['push', 'constant', '2'], 'file': 'FibonacciSeries', 'num': '16'}
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
@ARG   //{'code': ['pop', 'argument', '0'], 'file': 'FibonacciSeries', 'num': '18'}
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
(LOOP)   //{'code': ['label', 'LOOP'], 'file': 'FibonacciSeries', 'num': '20'}
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'FibonacciSeries', 'num': '21'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['if-goto', 'COMPUTE_ELEMENT'], 'file': 'FibonacciSeries', 'num': '22'}
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
@END   //{'code': ['goto', 'END'], 'file': 'FibonacciSeries', 'num': '23'}
0;JMP
(COMPUTE_ELEMENT)   //{'code': ['label', 'COMPUTE_ELEMENT'], 'file': 'FibonacciSeries', 'num': '25'}
@THAT   //{'code': ['push', 'that', '0'], 'file': 'FibonacciSeries', 'num': '27'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@THAT   //{'code': ['push', 'that', '1'], 'file': 'FibonacciSeries', 'num': '28'}
D=M
@1
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
@THAT   //{'code': ['pop', 'that', '2'], 'file': 'FibonacciSeries', 'num': '30'}
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
@THAT   //{'code': ['push', 'pointer', '1'], 'file': 'FibonacciSeries', 'num': '32'}
D=M
@SP
M=M+1
A=M-1
M=D
@1   //{'code': ['push', 'constant', '1'], 'file': 'FibonacciSeries', 'num': '33'}
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
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'FibonacciSeries', 'num': '35'}
M=M-1
A=M
D=M
@THAT
M=D
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'FibonacciSeries', 'num': '37'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@1   //{'code': ['push', 'constant', '1'], 'file': 'FibonacciSeries', 'num': '38'}
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
@ARG   //{'code': ['pop', 'argument', '0'], 'file': 'FibonacciSeries', 'num': '40'}
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
@LOOP   //{'code': ['goto', 'LOOP'], 'file': 'FibonacciSeries', 'num': '41'}
0;JMP
(END)   //{'code': ['label', 'END'], 'file': 'FibonacciSeries', 'num': '43'}