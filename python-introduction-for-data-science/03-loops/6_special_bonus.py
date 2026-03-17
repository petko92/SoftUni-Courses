#Read user input
stop_number = int(input())

#Logic
previous_number = 0
current_number = 0

while stop_number > 0:
    current_number = int(input())
    if current_number == stop_number:
        special_bonus = previous_number * 1.2 #20% increase
        print(int(special_bonus))
        break

    previous_number = current_number #прочитаме ново число, за да не изпаднем в безкраен цикъл

"""
6.	Special Bonus
Write a program to apply a 20% bonus for certain number:
•	Reads an integer number from the console: the "stop number"
•	Keep reading integers until it finds the stop number
•	When the stop number is found, increase the value of the previous number before it with 20% and print it
Input
25   #stop number
20
30   #previous number -> increase 20% (36)
25   #stop number
Output
36
"""