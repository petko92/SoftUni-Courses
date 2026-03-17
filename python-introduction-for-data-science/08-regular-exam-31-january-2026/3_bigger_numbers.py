user_input = input().split()
n = int(input())
bigger_numbers = []
for num in user_input:
    if int(num) > n:
        bigger_numbers.append(str(num))
print(f"{' '.join(bigger_numbers)}")

'''
Bigger Numbers
Write a program that:
•	Reads a list with integer numbers (separated with single space) from the first line of the console
•	Reads an integer number N from the second line of the console
•	Print the all numbers from the list, which are bigger than number N, separated by single space
Example Input / Output
Input	                  Output	Comments
1 2 3 4 5 6
3	                  4 5 6	                  Numbers from list, bigger than 3: 4, 5, 6
10 12 43 56 87
26	                  43 56 87	                  Numbers from list, bigger than 26: 43, 56, 87

'''