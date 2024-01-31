// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code

//initialize variables 

    @SCREEN
    D=A

    @screenLocation
    M=D

    @KBD
    D=A

    @endOfScreen
    M=D-1

//Wait for keypress  
(WAIT)
    @KBD
    D=M

    @STARTFILL 
    D;JNE


    @STARTEMPTY
    0;JMP

//Fill screen

(STARTFILL)
    @SCREEN
    D=A

    @screenLocation
    M=D

(FILL)
    
    @screenLocation
    A=M

    M=-1

    @screenLocation
    M = M+1

    D=M
    @endOfScreen
    D=M-D

    @FILL
    D;JGE

    @WAIT
    0;JMP


//Empty screen
(STARTEMPTY)
    @SCREEN
    D=A

    @screenLocation
    M=D

(EMPTY)
    
    @screenLocation
    A=M

    M=0

    @screenLocation
    M = M+1

    D=M
    @endOfScreen
    D=M-D

    @EMPTY
    D;JGE

    @WAIT
    0;JMP
    