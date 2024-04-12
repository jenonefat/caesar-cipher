# caesar-cipher

## Overview:
  This project is based on a problem set from an undergraduate MIT course, 'Introduction to Computer Science and Programming in Python'. 
  The purpose of this problem set is to reinforce the following concepts: **recursive solutions, dictionaries, classes, and inheritance.**
  
## Project Goal: 
    To build a program that can encrypt(encode) or decrypt(decode) a message. 

### Permutations

### Part B
    In file *pset4b_official*, I built a parent class (Message), and two subclasses of the parent class(PlaintextMessage and CiphertextMessage). 
  #### Message class 
    ~ contains data attributes & methods inherited by both subclasses 
  #### PlaintextMessage class 
    ~ contains methods to **encrypt a string message** given a *shift* integer; every letter in the message will shift 
    down the alphabet however many places as specified by the integer value. Punctuation and the letter case(uppercase or lowercase) is kept the same.
    The PlaintextMessage class also contains methods to change the cipher message by changing the shift value. 
    
  #### CiphertextMessage class 
    ~ contains methods to **decode** an encrypted message to reveal the original text. 
     
