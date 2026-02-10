# Read user input
num1 = int(input())
num2 = int(input())
operator = input()

# Logic
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print('Error! Possible given values for the math operator are: "+", "-", "*", "/"')
    exit()
# Print result
print(f"{num1} {operator} {num2} = {result:.2f}")

# Variant II - Cannot divide by zero
# # Read user input
# num1 = int(input())
# num2 = int(input())
# operator = input()
#
# # Logic
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero"
#
# # Print result
# if operator == "/" and num2 == 0:
#     print(f"{num1} {operator} {num2} = {result}")
# else:
#     print(f"{num1} {operator} {num2} = {result:.2f}")