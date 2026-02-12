#Read user input
first_number = int(input())
second_number = int(input())
third_number = int(input())

#Logic

# def three_numbers(num_1, num_2, num_3):
#     return min(num_1, num_2, num_3)
#
# result = three_numbers(first_number, second_number, third_number)
#
# print(result)


def three_numbers(num_1:int, num_2:int, num_3:int)-> int:
    smallest = num_1

    if num_2 < smallest:
        smallest = num_2

    if num_3 < smallest:
        smallest = num_3
    return smallest

result = three_numbers(first_number, second_number, third_number)

#Print output
print(result)