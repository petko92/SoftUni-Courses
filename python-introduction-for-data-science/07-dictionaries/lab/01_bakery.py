#Read user input
user_input = input().split(' ')

#Logic
my_dict = {}

while len(user_input) != 0:
    food = user_input.pop(0)
    quantity = user_input.pop(0)

    my_dict[food] = int(quantity)

#Print output
print(my_dict)