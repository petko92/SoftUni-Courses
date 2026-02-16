#Read user input
text = input()
vowels = 'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'
output = ""
#Logic, Print result
for i in range(len(text)):
    if not text[i] in vowels:
        print(text[i], end="")



"""
Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. 
Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

Examples
Input	           Output
Python	           Pythn
ILovePython	       LvPythn

"""