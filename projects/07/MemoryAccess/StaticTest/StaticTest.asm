@111   //['push', 'constant', '111']
D=A
@SP
A=M
M=D
@SP
M=M+1
@333   //['push', 'constant', '333']
D=A
@SP
A=M
M=D
@SP
M=M+1
@888   //['push', 'constant', '888']
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP   //['pop', 'static', '8']
M=M-1
A=M
D=M
@MemoryAccessStaticTestStaticTest.vm.8
M=D
@SP   //['pop', 'static', '3']
M=M-1
A=M
D=M
@MemoryAccessStaticTestStaticTest.vm.3
M=D
@SP   //['pop', 'static', '1']
M=M-1
A=M
D=M
@MemoryAccessStaticTestStaticTest.vm.1
M=D
@MemoryAccessStaticTestStaticTest.vm.3   //['push', 'static', '3']
D=M
@SP
M=M+1
A=M
A=A-1
M=D
@MemoryAccessStaticTestStaticTest.vm.1   //['push', 'static', '1']
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
@MemoryAccessStaticTestStaticTest.vm.8   //['push', 'static', '8']
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