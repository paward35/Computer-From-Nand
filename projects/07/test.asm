//load constant into D
@7 
D=A
//Select location of stack head
@SP
A=M
//Load value into stack head
M=D
//increment stack head
@SP
M=M+1

//load constant into D
@8
D=A
//Select location of stack head
@SP
A=M
//Load value into stack head
M=D
//increment stack head
@SP
M=M+1


//ADD
//decrement stack head
@SP
M=M-1
//Point M at stack head
//Move to pointer address and save in D
A=M 
//Load Value at stack head
D=M 
//decrement stack head
@SP
M=M-1
//Point M at stack head
A=M
//set stack head
M=D+M
@SP
M=M+1



