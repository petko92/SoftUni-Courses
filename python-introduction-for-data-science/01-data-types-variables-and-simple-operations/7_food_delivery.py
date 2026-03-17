# Read user input
number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegetarian_menus = int(input())

# Logic
CHICKEN_MENU_COST = 10.35
FISH_MENU_COST = 12.40
VEGETARIAN_MENU_COST = 8.15

price_chicken_menus = number_chicken_menus * CHICKEN_MENU_COST
price_fish_menus = number_fish_menus * FISH_MENU_COST
price_vegetarian_menu = number_vegetarian_menus * VEGETARIAN_MENU_COST
sum_of_menus = price_chicken_menus + price_fish_menus + price_vegetarian_menu
DELIVERY_PRICE = 2.50
dessert = sum_of_menus * 0.2
order_price = sum_of_menus + DELIVERY_PRICE + dessert
# Print result
print(order_price)

"""
7. Food Delivery
The restaurant opens its doors and offers several menus at preferential prices: 
•	Chicken menu – 10.35 lv. 
•	Menu with fish – 12.40 lv. 
•	Vegetarian menu – 8.15 lv. 
Write a program that calculates how much it will cost a group of people to order takeaways.
The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery). 
The delivery price is 2.50 BGN and is finally charged.  
Input
From the console read 3 lines:
•	Number of chicken menus – integer in the range [0 ... 99]
•	Number of menus with fish – integer in the range [0 ... 99]
•	Number of vegetarian menus – an integer in the range [0 ... 99]
Output
Print out only one line on the console: "{order price}"
Example Input / Output
Input
2
4
3
Output
116.2
"""