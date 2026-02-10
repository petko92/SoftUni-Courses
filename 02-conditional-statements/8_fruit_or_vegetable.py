# Read User input
product = input()

# Logic, Print result
fruits = "banana", "apple", "kiwi", "cherry", "lemon"
vegetables = "cucumber", "pepper", "carrot"

if product in fruits:
    print("fruit")
elif product in vegetables:
    print("vegetable")
else:
    print("unknown")

"""
8.	Fruit or Vegetable
Write a program that:
•	Reads a product (string) from the console
•	Based on type of the given product, print:
o	If product is one of following "banana", "apple", "kiwi", "cherry" or "lemon" you have to print "fruit"
o	If product is one of following "cucumber", "pepper" or "carrot" you have to print "vegetable"
o	If the product is different from listed products above, print "unknown"


Input	Output		Input	Output	        Input	Output
banana	fruit		pepper	vegetable		table	unknown

"""