#Read user input
search = input()
text = input()

#Logic
while search in text:
    text = text.replace(search,"")

#Print output
print(text)