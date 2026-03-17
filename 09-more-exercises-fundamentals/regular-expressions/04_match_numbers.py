from re import finditer

#Read user input
text = input()

#Logic
expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = finditer(expression,text)

output = []

for match in matches:
    output.append(match.group())

#Print result
print(", ".join(output))