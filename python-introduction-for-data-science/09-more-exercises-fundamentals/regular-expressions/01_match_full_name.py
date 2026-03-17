#RegEx library
import re

#Read user input
text = input()

#Logic
matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",text)

#Print output
print(" ".join(matches))


'''
Find full name:
Input: 
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith Peter SmIth, Lily Everett
Output: 
Peter Smith Lily Everett
'''