#Read user input
names_list = input().split(", ")

#Logic
sorted_list = sorted(names_list, key=lambda x: (-len(x), x ))

#Print output
print(sorted_list)