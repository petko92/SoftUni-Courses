text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isalnum():     #digits or letters
        if ch.isdigit():
            digits += ch
        else:
            letters += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)

#isdigit() - 12345
#isalpha() - letters - lower or upper (a-Z ASCII table)
#isalnum() - digits or letters
#isupper() - A
#islower(  - a
