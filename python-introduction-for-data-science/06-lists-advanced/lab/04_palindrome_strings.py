#Read user input
words = input().split(" ")
searched_word = input()

#Logic

filtered_list = [w for w in words if "".join(reversed(w)) == w]

#Print output

print(filtered_list)
print(f"Found palindrome {filtered_list.count(searched_word)} times")