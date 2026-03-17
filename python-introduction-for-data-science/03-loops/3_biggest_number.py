from math import inf
#Read user input
n = int(input())

#Logic
biggest = -inf
for i in range(n):
    num = int(input())
    if num > biggest:
        biggest = num
#Print result
print(biggest)