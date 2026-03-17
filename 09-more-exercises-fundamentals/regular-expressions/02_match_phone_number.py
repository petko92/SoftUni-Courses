import re

#Read user input
text = input()

#Logic
matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", text)

#Print output
print(" ".join(matches))


'''
Variant II optimization - solution with finditer() and group()

text = input()
matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

output = []

for match in matches:
    output.append(match.group())
    
print(", ".join(output))

'''

'''
Input:
+359 2 222 2222, 359-2-222-2222, +359/2/222/2222, +359-2 222 2222, +359 2-222-2222, +359-2-222-222, +359-2-222-22222, +359-2-222-2222
Output:
+359 2 222 2222 +359-2-222-2222
'''


