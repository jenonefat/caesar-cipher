# caesar-cipher

## Overview:
  This project is based on a problem set from an undergraduate MIT course, 'Introduction to Computer Science and Programming in Python'. 
  The purpose of this problem set is to reinforce the following concepts: **recursive solutions, dictionaries, classes, and inheritance.**
  
## Project Goal: 
    To build a program that can encrypt(encode) or decrypt(decode) a message. 

### Permutations
  ~ File 'permutations' contains a function that returns all the possible permutations of a string. 
  ~ uses recursive method- I tried my best to explain the code in the comments, but I've found that 
  the best way to understand a recursive solution is to write/draw it out!!! 
  
### Part B
    In file pset4b_official, I built a program containing a parent class (Message), and two subclasses of 
    the parent class(PlaintextMessage and CiphertextMessage). 
  #### Message class 
    ~ contains data attributes & methods inherited by both subclasses 
  #### PlaintextMessage class 
    ~ encrypts a string message given a shift integer; 
    every letter in the message will shift down the alphabet however many 
    places as specified by the integer value. 
    Punctuation and the letter case(uppercase or lowercase) is kept the same.
    The PlaintextMessage class also contains methods to change the cipher message by changing the shift value. 
    
  #### CiphertextMessage class 
    ~ contains methods to decode an encrypted message to reveal the original text. 

### Part C
   File pset4c_official contains the parent class, SubMessage(short for 'Substitution Message')
   and the child class EncryptedSubMessage. 
  #### SubMessage class 
    ~ encrypts a string message by replacing every vowel with another as specified by the input vowel permutation
    ~ consonants, punctuation and letter case(uppercase or lowercase) remain unaltered in the cipher 
  #### EncryptedSubMessage class
    ~ decrypts an encoded string message to reveal the original text by checking every possible permutation
    of vowels 
    ~ 
     
