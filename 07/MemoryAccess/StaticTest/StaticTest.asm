//push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop static 8
@SP
M=M-1
A=M
D=M
@static8
M=D
//pop static 3
@SP
M=M-1
A=M
D=M
@static3
M=D
//pop static 1
@SP
M=M-1
A=M
D=M
@static1
M=D
//push static 3
@static3
D=M
@SP
A=M
M=D
@SP
M=M+1
//push static 1
@static1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
//push static 8
@static8
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
