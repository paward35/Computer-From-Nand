@256
D=A
@SP
M=D
@returnAddressSys.init.0     // {'code': ['call', 'Sys.init', '0'], 'file': 'Sys', 'num': '0'}
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
(returnAddressSys.init.0)
(Main.fibonacci)//{'code': ['function', 'Main.fibonacci', '0'], 'file': 'Main', 'num': '11'}
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'Main', 'num': '12'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@2   //{'code': ['push', 'constant', '2'], 'file': 'Main', 'num': '13'}
D=A
@SP
M=M+1
A=M-1
M=D
@SP  //{'code': ['lt'], 'file': 'Main', 'num': '14'}
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@ISlt14
D;JLT
@SP
A=M-1
M=0
@SKIPlt14
0;JMP
(ISlt14)
@SP
A=M-1
M=-1
(SKIPlt14)
@SP  //{'code': ['if-goto', 'N_LT_2'], 'file': 'Main', 'num': '15'}
M=M-1
A=M
D=M
@N_LT_2
D;JNE
@N_GE_2   //{'code': ['goto', 'N_GE_2'], 'file': 'Main', 'num': '16'}
0;JMP
(N_LT_2)   //{'code': ['label', 'N_LT_2'], 'file': 'Main', 'num': '17'}
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'Main', 'num': '18'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@LCL  //{'code': ['return'], 'file': 'Main', 'num': '19'}
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
(N_GE_2)   //{'code': ['label', 'N_GE_2'], 'file': 'Main', 'num': '20'}
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'Main', 'num': '21'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@2   //{'code': ['push', 'constant', '2'], 'file': 'Main', 'num': '22'}
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
@returnAddressMain.fibonacci.24     // {'code': ['call', 'Main.fibonacci', '1'], 'file': 'Main', 'num': '24'}
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
@Main.fibonacci
0;JMP
(returnAddressMain.fibonacci.24)
@ARG   //{'code': ['push', 'argument', '0'], 'file': 'Main', 'num': '25'}
D=M
@0
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
@1   //{'code': ['push', 'constant', '1'], 'file': 'Main', 'num': '26'}
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
@returnAddressMain.fibonacci.28     // {'code': ['call', 'Main.fibonacci', '1'], 'file': 'Main', 'num': '28'}
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
@Main.fibonacci
0;JMP
(returnAddressMain.fibonacci.28)
@SP  //add
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
@LCL  //{'code': ['return'], 'file': 'Main', 'num': '30'}
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
(Sys.init)//{'code': ['function', 'Sys.init', '0'], 'file': 'Sys', 'num': '42'}
@4   //{'code': ['push', 'constant', '4'], 'file': 'Sys', 'num': '43'}
D=A
@SP
M=M+1
A=M-1
M=D
@returnAddressMain.fibonacci.44     // {'code': ['call', 'Main.fibonacci', '1'], 'file': 'Sys', 'num': '44'}
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
@Main.fibonacci
0;JMP
(returnAddressMain.fibonacci.44)
(END)   //{'code': ['label', 'END'], 'file': 'Sys', 'num': '45'}
@END   //{'code': ['goto', 'END'], 'file': 'Sys', 'num': '46'}
0;JMP