# Read user input
quantity_nylon = int(input()) + 2 # + 2 sq.m
quantity_paint = int(input()) * 1.1 # +10%
quantity_of_thinner = int(input())
hours_working = int(input())

# Logic
PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_PAINT_THINNER = 5.00
BAGS = 0.40


amount_of_nylon = quantity_nylon * PRICE_NYLON
amount_of_paint = quantity_paint * PRICE_PAINT
amount_of_thinner = quantity_of_thinner * PRICE_PAINT_THINNER
total_amount = amount_of_nylon + amount_of_paint + amount_of_thinner + BAGS
money_craftsmen = total_amount * hours_working * 0.30

sum_of_all_costs = total_amount + money_craftsmen
# Print result
print(sum_of_all_costs)


"""
6. Redecorating
Rumen wants to repaint the living room and has hired craftsmen for this purpose. Write a program that calculates the cost of the repair, taking the following prices for the calculation:
•	Protective nylon - 1.50 BGN per square meter
•	Paint - 14.50 BGN per liter
•	Paint thinner - 5.00 BGN per liter
Just in case, to the necessary materials, Rumen wants to add another 10% of the amount of paint and 2 square meters of nylon, also 0.40 leva for bags. The amount paid to the craftsmen for 1 hour of work is equal to 30% of the sum of all material costs. 
Input
The input is read from the console and contains exactly 4 lines:
1.	Required amount of nylon (in sq.m.) - an integer number in the range [1... 100]
2.	Required amount of paint (in liters) - an integer number in the range [1... 100]
3.	Quantity of thinner (in liters) - integer number in the range [1... 30]
4.	Hours needed for the craftsmen to do the work - an integer number in the range [1... 9]
Output
Print out only one line on the console:
•	"{the sum of all costs}"
Input
10
11
4
8
Output
727.09
"""