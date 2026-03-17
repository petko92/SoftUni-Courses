#Read user input
words = input().split()

#Logic
output = ""
for word in words:
    output += word * len(word)

#Print output
print(output)

