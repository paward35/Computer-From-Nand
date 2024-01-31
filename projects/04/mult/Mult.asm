
    @R2 
    M=0



(LOOP)
    @R0
    D=M

    @STOP
    D;JEQ

    @R0
    M = M - 1

    @R1 
    D=M

    @R2 
    M=D+M

    @LOOP
    0;JMP
    

(STOP)
    @STOP
    0;JMP