@10   //['push', 'constant', '10']
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL   //['pop', 'local', '0']
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
@21   //['push', 'constant', '21']
D=A
@SP
A=M
M=D
@SP
M=M+1
@22   //['push', 'constant', '22']
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG   //['pop', 'argument', '2']
D=M
@2
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
@ARG   //['pop', 'argument', '1']
D=M
@1
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
@36   //['push', 'constant', '36']
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS   //['pop', 'this', '6']
D=M
@6
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
@42   //['push', 'constant', '42']
D=A
@SP
A=M
M=D
@SP
M=M+1
@45   //['push', 'constant', '45']
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT   //['pop', 'that', '5']
D=M
@5
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
@THAT   //['pop', 'that', '2']
D=M
@2
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
@510   //['push', 'constant', '510']
D=A
@SP
A=M
M=D
@SP
M=M+1
@5   //['pop', 'temp', '6']
D=A
@6
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
@THAT   //['push', 'that', '5']
D=M
@5
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
@ARG   //['push', 'argument', '1']
D=M
@1
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
M=M-D
@SP
M=M+1
@THIS   //['push', 'this', '6']
D=M
@6
A=D+A
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@THIS   //['push', 'this', '6']
D=M
@6
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
@5   //['push', 'temp', '6']
D=A
@6
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