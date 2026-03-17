# Read user input
num1 = float(input())
num2 = float(input())
num3 = float(input())

# Logic, Print result
""""
The number of negative numbers determines the sign:

0 or 2 negative numbers -> positive product

1 or 3 negative numbers -> negative product
"""

if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
else:

    negative_count = 0

    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1
    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")
