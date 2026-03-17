#Read user input
numbers = list(map(int, input().split(", ")))
#Logic
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
    if num < 0:
        negative_numbers.append(num)
    if num % 2 == 0:
        even_numbers.append(num)
    if num % 2 != 0:
        odd_numbers.append(num)

#Print output
print(f"Positive: {', '.join(map(str, positive_numbers))}")
print(f"Negative: {', '.join(map(str, negative_numbers))}")
print(f"Even: {', '.join(map(str, even_numbers))}")
print(f"Odd: {', '.join(map(str, odd_numbers))}")

#Optimization solution with list comprehension

"""
numbers = list(map(int, input().split(", ")))
.
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")
"""

"""
4.	Number Classification
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", 
and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
Note: Zero is counted as a positive number
Examples
Input	                                            Output
1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33	Positive: 1, 0, 5, 3, 4, 12, 19
                                            Negative: -2, -100, -20, -33
                                            Even: -2, 0, 4, -100, -20, 12
                                            Odd: 1, 5, 3, 19, -33

"""



