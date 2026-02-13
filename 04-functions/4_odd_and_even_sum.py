#Read user input
single_number = int(input())

#Logic
def sum_even_odd_digits(number:int) -> str:
    odd_sum = 0
    even_sum = 0

    for n in str(abs(number)):
        digit = int(n)

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

result = sum_even_odd_digits(single_number)

#Print output
print(result)