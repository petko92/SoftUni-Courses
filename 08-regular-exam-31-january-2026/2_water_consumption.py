# count_of_days = int(input())
#
# quantity_water = [int(input()) for _ in range(count_of_days)]
#
# cumulative_sum = 0
# for i in range(count_of_days):
#     cumulative_sum += quantity_water[i]
#     print(cumulative_sum)

count_of_days = int(input())

if count_of_days <= 0:
    print(0)
else:
    cumulative_sum = 0
    for _ in range(count_of_days):
        daily_water = int(input())
        cumulative_sum += daily_water
        print(cumulative_sum)

'''
Water Consumption
Write a program that:
•	Reads an integer number N (count of the days) from the console.
•	For each day (from first to the last (N)):
o	Read from the console the amount of water consumed (integer number in milliliters) on that day.
o	Calculate the cumulative water consumption after adding each day's intake.
o	Print the cumulative water consumption on a separate line.
o	In case of N equal to or less than zero, print zero as the result.

Input	  Output
4
500
600
700
800	   500
       1100
       1800
       2600

'''