# Read User Input
time_1 = int(input())
time_2 = int(input())
time_3 = int(input())
# Logic, Print result

minutes = (time_1 + time_2 + time_3) // 60
seconds = (time_1 + time_2 + time_3) % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

""""
9.	Sum Seconds
Three athletes finish in a certain number of seconds (between 1 and 50). 
Write a program that:
•	Read three integers - the athletes' times in seconds, from console
•	 Calculate their total time in the format "minutes:seconds"
Note: The seconds should be displayed with leading zero (2 as "02", 7 as "07", 35 as "35").
Example

Input	
35
45
44	
Output
2:04

Input
50
50
49
Output
2:29


"""