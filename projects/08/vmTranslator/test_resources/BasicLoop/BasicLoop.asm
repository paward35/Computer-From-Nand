@0   //['push', 'constant', '0']
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL   //['pop', 'local', '0', '', '', '', '', '', '', '', '', '']
D=M
@0
D=D+A
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1
(LOOP)   //['label', 'LOOP']
@ARG   //['push', 'argument', '0']
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@LCL   //['push', 'local', '0']
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@SP   //{op}
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
@LCL   //['pop', 'local', '0', '', '', '', '', '', '', '', '']
D=M
@0
D=D+A
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1
@ARG   //['push', 'argument', '0']
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@1   //['push', 'constant', '1']
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   //{op}
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
@ARG   //['pop', 'argument', '0', '', '', '', '', '', '']
D=M
@0
D=D+A
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
M=M-1
@ARG   //['push', 'argument', '0']
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@SP   //['if-goto', 'LOOP', '', '', '', '', '', '', '', '']
M=M-1
A=M
D=M
@LOOP
D;JNE
@LCL   //['push', 'local', '0', '', '', '', '', '', '', '', '']
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D