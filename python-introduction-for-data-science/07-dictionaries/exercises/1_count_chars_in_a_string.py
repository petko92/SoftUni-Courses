#Read user input
text = input()

#Logic
#char_counts = {}

char_counts = {letter: text.count(letter) for letter in text if letter != ' '}
'''
for letter in text:
    if letter == ' ':
        continue

    if letter not in char_counts:
        char_counts[letter] = 0

    char_counts[letter] += 1
'''
#Extract data, Print output
for char, count in char_counts.items():
    print(f'{char} -> {count}')


'''
1.	Count Chars in a String
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"
Examples
Input	            Output
text	            t -> 2
                    e -> 1
                    x -> 1
text text text
	                t -> 6
                    e -> 3
                    x -> 3

'''