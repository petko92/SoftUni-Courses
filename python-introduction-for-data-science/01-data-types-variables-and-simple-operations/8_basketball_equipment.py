# Read user input
annual_training_fee = int(input())

# Logic
basketball_sneakers = annual_training_fee * 0.60 # 40 % less than the fee for one year
basketball_team = basketball_sneakers * 0.80 # 20% cheaper than that of sneakers
basketball = basketball_team / 4
basketball_accessoaries = basketball / 5

money_of_spend_for_basketball = annual_training_fee + basketball_sneakers + basketball_team + basketball + basketball_accessoaries
# Print result
print(money_of_spend_for_basketball)
"""
8. Basketball Equipment
Jesse decides he wants to play basketball, but he needs equipment to train. Write a program that calculates the expenses of Jesse if he starts training, knowing how much is the fee for basketball training for a period of 1 year. 
•	Basketball sneakers – their price is 40% less than the fee for one year
•	Basketball team – its price is 20% cheaper than that of sneakers
•	Basketball – its price is 1 / 4 of the price of the basketball team
•	Basketball accessories – their price is 1 / 5 of the price of the basketball
Input
From the console read 1 row:
•	The annual basketball training fee – an integer in the range [0... 9999]
Output
Print on the console how much Jesse will spend if he starts playing basketball.
Example Input / Output
Input
365
Output
811.76
"""