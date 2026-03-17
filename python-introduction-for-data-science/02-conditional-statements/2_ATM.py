# Read user input
balance = int(input())
withdraw = int(input())
limit = int(input())

# Logic, Print result
if withdraw > limit:
    print("The limit was exceeded.")
elif withdraw > balance:
    print("Insufficient availability.")
else:
    print("The withdraw was successful.")

"""    
Input	
420
20
25
Output	
The withdraw was successful.

Input
10
50
20
Output
The limit was exceeded.

Input
10
20
30
Output	
Insufficient availability.	
	
560
10
35
Output
The withdraw was successful.
"""
