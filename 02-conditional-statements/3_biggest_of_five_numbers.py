# Read user input
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# Logic
biggest = num1

if num2 > biggest:
    biggest = num2

if num3 > biggest:
    biggest = num3

if num4 > biggest:
    biggest = num4

if num5 > biggest:
    biggest = num5

# Print result
print(biggest)