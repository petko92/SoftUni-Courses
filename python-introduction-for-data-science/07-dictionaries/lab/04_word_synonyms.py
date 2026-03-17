#Read user input
n = int(input())

#Logic
synonyms = {}

for i in range(n):
    word = input()
    s = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(s)


for k, v in synonyms.items():
    print(f"{k} - {', '.join(v)}")



