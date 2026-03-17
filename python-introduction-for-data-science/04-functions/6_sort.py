#Read user input
sequence_of_numbers = input()

#Logic
def sorting(sequence:str) -> list[int]:
    numbers = list(map(int, sequence_of_numbers.split()))
    sort_numbers = sorted(numbers)
    return sort_numbers

result = sorting(sequence_of_numbers)

#Print output
print(result)
