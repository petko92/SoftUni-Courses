#Read user input
text = input()

#Logic, Print output
while not text == "end":
    rev = reversed(text)
    reversed_text = "".join(rev)
    print(f"{text} = {reversed_text}")

    text = input()

'''
#reversed text with list slicing method

reversed_text = text[::-1]
print(f"{text} = {reversed_text}")

'''

# rev = list(reversed(text))
# print(''.join(rev))
