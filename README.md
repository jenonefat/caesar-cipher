# caesar-cipher

## Overview:
  This project is based on a problem set from an undergraduate MIT course, 'Introduction to Computer Science and Programming in Python'. 
  The purpose of this problem set is to reinforce the following concepts: **recursive solutions, dictionaries, classes, and inheritance.**
  Code components provided by MIT instructors: function names, function docstrings, 'story.txt' file, 'words.txt' file, 
 helper functions(load_words(), is_word(), get_story_string()) 
## Project Goal: 
    To build a program that can encrypt(encode) or decrypt(decode) messages using two distinct methods 

### Permutations
  - File 'permutations' contains a function that returns all the possible permutations of a string. 
  - uses recursive method- I tried my best to explain the code in the comments, but I've found that 
  the best way to understand a recursive solution is to write/draw it out!!! 
  
### Part B
  - file pset4b_official contains a program that encodes and decodes string messages by shifting 
    all the letters down the alphabet 
  - includes a parent class (Message), and two subclasses of the parent class(PlaintextMessage and CiphertextMessage). 
  #### Message class 
    ~ contains data attributes & methods inherited by both subclasses 
  #### PlaintextMessage class 
    - encrypts a string message given a shift integer; 
    every letter in the message will shift down the alphabet however many 
    places as specified by the integer value. 
    - punctuation and the letter case(uppercase or lowercase) is kept the same.
    - the PlaintextMessage class also contains methods to change the cipher message by changing the shift value. 
    
  #### CiphertextMessage class 
    - decodes an encrypted message to reveal the original text 
    - checks each of the 26 possible shifts used to encrypt the original message by shifting the decrypted message 26-shift places
      - for example, if the plaintext message was shifted down the alphabet by 1 position, then shifting each letter in the cipher 
      by 25 places should yield the original letters 
### Part C
   - file pset4c_official contains a program that encodes and decodes string messages by substituting vowels 
   - contains the parent class, SubMessage(short for 'Substitution Message')
   and the child class EncryptedSubMessage
  - even though substituting all the letters would objectively yield better encryptions,
    the problem set only called for vowel substitutions for the sake of brevity and convenience: if both consonants
    and vowels were substituted, then the program would have to iterate through 26 factorial distinct permutations to
    decrypt a message
  #### SubMessage class 
    - encrypts a string message by replacing every vowel with another as specified by the input vowel permutation
    - consonants, punctuation and letter case(uppercase or lowercase) remain unaltered in the cipher 
  #### EncryptedSubMessage class
    - decrypts an encoded string message to reveal the original text by substituting with every possible
    permutation of vowels to find the one that yields the greatest number of valid words
    - this is where I apply the 'get_permutations(string)' function from the 'permutations' file!!! 
     
