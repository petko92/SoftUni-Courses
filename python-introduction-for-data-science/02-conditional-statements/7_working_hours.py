# Read user Input
working_time_start = int(input())
day_of_week = input()

#Logic, Print result
if not day_of_week == "Sunday" and working_time_start >= 10 and working_time_start <= 18:
    print("open")
else:
    print("closed")

# Variant II
""""
# Read user Input
working_time_start = int(input())
day_of_week = input()
#Logic, Print result
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

if day_of_week in days and working_time_start >= 10 and working_time_start <= 18:
    if not day_of_week == "Sunday":
        print("open")
    elif day_of_week == "Sunday":
        print("closed")
else:
    if day_of_week not in days:
        print("Invalid day!")
    else:
         print("closed")

"""
