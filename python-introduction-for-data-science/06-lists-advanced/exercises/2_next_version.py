# # Read user input
# version = list(map(int, input().split(".")))
#
# # Logic
# n1, n2, n3 = version
#
# n3 += 1
#
# if n3 >= 9:
#     n3 = 0
#     n2 += 1
#
# if n2 >= 9:
#     n2 = 0
#     n1 += 1
#
# # Print output
# print(f"{n1}.{n2}.{n3}")

#Read user input
version = list(map(int, input().split(".")))

#Logic
version[2] += 1

for i in range(2, 0, -1):
    if version[i] > 9:
        version[i] = 0
        version[i-1] += 1

#Print output
print(f"{version[0]}.{version[1]}.{version[2]}")

"""
2.	Next Version
You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number.
 For more clarification, see the examples below.
Note: there will be no case in which the first number will become greater than 9.

Input	Output
1.2.3	1.2.4
1.3.9	1.4.0
3.9.9	4.0.0

"""