#Read user input
first_number = int(input())
second_number = int(input())
third_number = int(input())

#Logic
def subtract(sum_result:int, c:int)->int:
    return sum_result - c

def sum_numbers(a, b):
    return a + b


def add_and_subtract(a:int, b:int, c:int)->int:
    amount = sum_numbers(a, b)
    result_subtract = subtract(amount, c)
    return result_subtract


result = add_and_subtract(first_number, second_number, third_number)

#Print output
print(result)