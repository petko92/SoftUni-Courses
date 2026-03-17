#Read user input
n = int(input())
word = input()

#Logic and Print result
my_list = []

for i in range(n):
    current_string = input()
    my_list.append(current_string)
print(my_list)

result = []
for sentence in my_list:
    if word in sentence:
        result.append(sentence)
print(result)