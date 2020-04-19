// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


//While Nothing is pressed
(NOTPRESSEDLOOP)
@KBD
D=M
@R0
M=D
@NOTPRESSEDLOOP
D;JEQ

@8191
D=A
@i
M=D

@SCREEN
D=A
@currentIndex
M=D

//make screen black
@SCREEN
D=A
M=-1
(PAINTINGSCREEN)
@currentIndex
M=M+1
A=M
M=-1

//loop back
@i
M=M-1
D=M
@PAINTINGSCREEN
D;JNE

//WhileSomething Is pressed
(PRESSEDLOOP)
@KBD
D=M
@PRESSEDLOOP
D;JNE

//PAINT WHITE
@8191
D=A
@i
M=D

@SCREEN
D=A
@currentIndex
M=D

//make screen white
@SCREEN
D=A
M=0
(PAINTINGSCREENWHITE)
@currentIndex
M=M+1
A=M
M=0

//loop back
@i
M=M-1
D=M
@PAINTINGSCREENWHITE
D;JNE

@NOTPRESSEDLOOP
D;JMP


//END
(END)
@END
D;JMP