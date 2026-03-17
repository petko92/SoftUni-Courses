#Read user input
num = int(input())
pow = int(input())
#Logic
result = 1
for _ in range(pow):
    result = result * num
#Print result
print(result)