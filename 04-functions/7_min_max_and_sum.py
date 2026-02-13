#Read user input
sequence_of_numbers = input()

#Logic
def min_max_and_sum(sequence:str) -> str:
    numbers = list(map(int, sequence_of_numbers.split()))
    min_number = min(numbers)
    max_number = max(numbers)
    sum_of_numbers = sum(numbers)

    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_numbers}"

result = min_max_and_sum(sequence_of_numbers)

#Print output
print(result)