# ---First way---

# Read user input
n = int(input())

# Logic and Print result
commands = ["even", "odd", "negative", "positive"]
even_list = []
odd_list = []
negative_list = []
positive_list = []

while True:
    data = input()

    if data in commands:
        if data == "even":
            print(even_list)
        elif data == "odd":
            print(odd_list)
        elif data == "positive":
            print(positive_list)
        else:  # negative
            print(negative_list)
        break
    else:
        # input is number
        number = int(data)
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

        if number >= 0:
            positive_list.append(number)
        else:
            negative_list.append(number)

"""
# --- Second way ---

# Read user input
n = int(input())

#Logic
my_list = []

for i in range(n):
    user_input = int(input())
    my_list.append(user_input)

filter = input()

filtered_list = []

for el in my_list:
    if filter == "even":
        if el % 2 == 0:
            filtered_list.append(el)
    elif filter == "odd":
        if el % 2 != 0:
            filtered_list.append(el)
    elif filter == "negative":
        if el < 0:
            filtered_list.append(el)
    elif filter == "positive":
        if el >= 0:
            filtered_list.append(el)

#Print result
print(filtered_list)
"""