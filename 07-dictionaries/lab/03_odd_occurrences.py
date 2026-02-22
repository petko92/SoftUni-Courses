#Read user input
words = input().split()

#Logic
result = {}
odd_items = []

for w in words:
    lower_word = w.lower()
    if lower_word not in result.keys():
        result[lower_word] = 1
    else:
        result[lower_word] += 1


for k, v in result.items():
    if v % 2 != 0:
        odd_items.append(k)

print(' '.join(odd_items))
