#Read user input
user_input = input().split()
searched_product = input().split()

#Logic
products = {}

while len(user_input) != 0:
    key = user_input.pop(0)
    value = user_input.pop(0)
    products[key] = int(value)

for p in searched_product:
    if p in products.keys():
        print(f"We have {products[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")





