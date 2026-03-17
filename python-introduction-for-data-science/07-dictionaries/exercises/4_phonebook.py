phonebook = {}
while True:
    line = input()

    if line.isdigit():
        num = int(line)
        break
    name, number = line.split("-")
    phonebook[name] = number

for _ in range(num):
    search_name = input()

    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")

    else:
        print(f"Contact {search_name} does not exist.")