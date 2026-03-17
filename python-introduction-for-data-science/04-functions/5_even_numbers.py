#Read user input
sequence_of_numbers = input()
numbers = list(map(int, sequence_of_numbers.split()))

#Logic
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

#Print result
print(even_numbers)
