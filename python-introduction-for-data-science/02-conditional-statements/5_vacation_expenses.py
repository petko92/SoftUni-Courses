# Read user input
season = input()
place = input()
count_days = int(input())

# Logic
price_per_night = 0
discount = 0
expenses = 0
total_expenses = 0

if season == "Winter" and place == "Hotel":
    price_per_night = 40
    expenses = count_days * price_per_night
    discount = 0.10 # 10%
    total_expenses = expenses * (1 - discount)
elif season == "Winter" and place == "Camping":
    price_per_night = 10
    expenses = count_days * price_per_night
    discount = 0.10
    total_expenses = expenses * (1 - discount)

if season == "Autumn" and place == "Hotel":
    price_per_night = 20
    expenses = count_days * price_per_night
    discount = 0.30 # 30%
    total_expenses = expenses * (1 - discount)
elif season == "Autumn" and place == "Camping":
    price_per_night = 15
    expenses = count_days * price_per_night
    discount = 0.30
    total_expenses = expenses * (1 - discount)

if season == "Summer" and place == "Hotel":
    price_per_night = 50
    total_expenses = count_days * price_per_night

elif season == "Summer" and place == "Camping":
    price_per_night = 30
    total_expenses = count_days * price_per_night

if season == "Spring" and place == "Hotel":
    price_per_night = 30
    expenses = count_days * price_per_night
    discount = 0.20 # 20%
    total_expenses = expenses * (1 - discount)
elif season == "Spring" and place == "Camping":
    price_per_night = 10
    expenses = count_days * price_per_night
    discount = 0.20
    total_expenses = expenses * (1 - discount)

# Print result
print(f"{total_expenses:.2f}")