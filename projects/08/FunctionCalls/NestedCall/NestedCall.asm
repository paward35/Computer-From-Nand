@256
D=A
@SP
M=D
@returnAddressSys.init     // {'code': ['call', 'Sys.init', '0'], 'file': 'Sys', 'num': '0'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(returnAddressSys.init)
(Sys.init)//{'code': ['function', 'Sys.init', '0'], 'file': 'Sys', 'num': '7'}
@4000   //{'code': ['push', 'constant', '4000'], 'file': 'Sys', 'num': '8'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '0'], 'file': 'Sys', 'num': '9'}
M=M-1
A=M
D=M
@THIS
M=D
@5000   //{'code': ['push', 'constant', '5000'], 'file': 'Sys', 'num': '10'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'Sys', 'num': '11'}
M=M-1
A=M
D=M
@THAT
M=D
@returnAddressSys.main     // {'code': ['call', 'Sys.main', '0'], 'file': 'Sys', 'num': '12'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(returnAddressSys.main)
@5   //{'code': ['pop', 'temp', '1'], 'file': 'Sys', 'num': '13'}
D=A
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
(LOOP)   //{'code': ['label', 'LOOP'], 'file': 'Sys', 'num': '14'}
@LOOP   //{'code': ['goto', 'LOOP'], 'file': 'Sys', 'num': '15'}
0;JMP
(Sys.main)//{'code': ['function', 'Sys.main', '5'], 'file': 'Sys', 'num': '24'}
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@4001   //{'code': ['push', 'constant', '4001'], 'file': 'Sys', 'num': '25'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '0'], 'file': 'Sys', 'num': '26'}
M=M-1
A=M
D=M
@THIS
M=D
@5001   //{'code': ['push', 'constant', '5001'], 'file': 'Sys', 'num': '27'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'Sys', 'num': '28'}
M=M-1
A=M
D=M
@THAT
M=D
@200   //{'code': ['push', 'constant', '200'], 'file': 'Sys', 'num': '29'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['pop', 'local', '1'], 'file': 'Sys', 'num': '30'}
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
@40   //{'code': ['push', 'constant', '40'], 'file': 'Sys', 'num': '31'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['pop', 'local', '2'], 'file': 'Sys', 'num': '32'}
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
@6   //{'code': ['push', 'constant', '6'], 'file': 'Sys', 'num': '33'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['pop', 'local', '3'], 'file': 'Sys', 'num': '34'}
D=M
@3
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
@123   //{'code': ['push', 'constant', '123'], 'file': 'Sys', 'num': '35'}
D=A
@SP
M=M+1
A=M-1
M=D
@returnAddressSys.add12     // {'code': ['call', 'Sys.add12', '1'], 'file': 'Sys', 'num': '36'}
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(returnAddressSys.add12)
@5   //{'code': ['pop', 'temp', '0'], 'file': 'Sys', 'num': '37'}
D=A
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
@LCL   //{'code': ['push', 'local', '0'], 'file': 'Sys', 'num': '38'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['push', 'local', '1'], 'file': 'Sys', 'num': '39'}
D=M
@1
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['push', 'local', '2'], 'file': 'Sys', 'num': '40'}
D=M
@2
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['push', 'local', '3'], 'file': 'Sys', 'num': '41'}
D=M
@3
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL   //{'code': ['push', 'local', '4'], 'file': 'Sys', 'num': '42'}
D=M
@4
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
@SP  //add
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
@SP  //add
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
@SP  //add
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
@LCL  //{'code': ['return'], 'file': 'Sys', 'num': '47'}
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP  
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
M=M-1
A=M
D=M
@THAT
M=D
@FRAME
M=M-1
A=M
D=M
@THIS
M=D
@FRAME
M=M-1
A=M
D=M
@ARG
M=D
@FRAME
M=M-1
A=M
D=M
@LCL
M=D
@RET
A=M
0;JMP
(Sys.add12)//{'code': ['function', 'Sys.add12', '0'], 'file': 'Sys', 'num': '50'}
@4002   //{'code': ['push', 'constant', '4002'], 'file': 'Sys', 'num': '51'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '0'], 'file': 'Sys', 'num': '52'}
M=M-1
A=M
D=M
@THIS
M=D
@5002   //{'code': ['push', 'constant', '5002'], 'file': 'Sys', 'num': '53'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['pop', 'pointer', '1'], 'file': 'Sys', 'num': '54'}
M=M-1
A=M
D=M
@THAT
M=D
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'Sys', 'num': '55'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@12   //{'code': ['push', 'constant', '12'], 'file': 'Sys', 'num': '56'}
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
@LCL  //{'code': ['return'], 'file': 'Sys', 'num': '58'}
D=M
@FRAME
M=D
@5
D=D-A
A=D
D=M
@RET
M=D
@SP  
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
M=M-1
A=M
D=M
@THAT
M=D
@FRAME
M=M-1
A=M
D=M
@THIS
M=D
@FRAME
M=M-1
A=M
D=M
@ARG
M=D
@FRAME
M=M-1
A=M
D=M
@LCL
M=D
@RET
A=M
0;JMP