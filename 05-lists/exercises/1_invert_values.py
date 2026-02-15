#Read user input
single_string = input()

#Logic
numbers = list(map(int, single_string.split()))

for i in range(len(numbers)):

    if numbers[i] < 0:
        numbers[i] = abs(numbers[i])
    else:
        numbers[i] = -abs(numbers[i])

#Print result
print(numbers)

"""
1.	Invert Values
Write a program that receives a single string containing positive and negative numbers separated by a single space.
Print a list containing the opposite of each number.


Example
Input	                    Output
1 2 -3 -3 5	          [-1, -2, 3, 3, -5]
-4 0 2 57 -101	      [4, 0, -2, -57, 101]

"""