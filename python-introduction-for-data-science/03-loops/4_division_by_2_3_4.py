#Read user input
n = int(input())

#Logic
count_div_by_2 = 0
count_div_by_3 = 0
count_div_by_4 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        count_div_by_2 += 1
    if num % 3 == 0:
        count_div_by_3 += 1
    if num % 4 == 0:
        count_div_by_4 += 1

percent_1 = (count_div_by_2 / n) * 100
percent_2 = (count_div_by_3 / n) * 100
percent_3 = (count_div_by_4 / n) * 100

#Print result
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")