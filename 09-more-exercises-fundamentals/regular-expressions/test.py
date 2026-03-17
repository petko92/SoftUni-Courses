import re

text = input()

matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",text)

print(" ".join(matches))


'''
Find full name:
Input: 
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith Peter SmIth, Lily Everett
Output: 
Peter Smith Lily Everett
'''