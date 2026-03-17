#Read user input
searched_words = input().split(", ")
sequence_of_strings = input().split(", ")

#Logic
found_words = []

for word in searched_words:
    for current_string in sequence_of_strings:
        if word in current_string:
            found_words.append(word)
            break

#Print output
print(found_words)

"""
searched_words = input().split(", ")
sequence_of_strings = input().split(", ")

result = [word for word in searched_words
          if any(word in string for string in sequence_of_strings)]

print(result)
"""





"""
1.	Which Are In?
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line.
Example
Input	                                             Output
arp, live, strong
lively, alive, harp, sharp, armstrong	             ['arp', 'live', 'strong']
tarp, mice, bull
lively, alive, harp, sharp, armstrong	             []

"""