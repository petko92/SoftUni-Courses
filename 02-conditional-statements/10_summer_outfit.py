# Read User Input
temperature = int(input())
time_of_day = input()

# Logic
stages_of_day = ("Morning", "Afternoon", "Evening")
clothing = None
shoes = None

if time_of_day in stages_of_day:
    if time_of_day == "Morning" and temperature >= 10:
        if temperature <= 18:
            clothing = "Sweatshirt"
            shoes = "Sneakers"
        elif temperature <= 24:
            clothing = "Shirt"
            shoes = "Moccasins"
        else:
            clothing = "T-Shirt"
            shoes = "Sandals"


    elif time_of_day == "Afternoon" and temperature >= 10:
        if temperature <= 18:
            clothing = "Shirt"
            shoes = "Moccasins"
        elif temperature <= 24:
            clothing = "T-Shirt"
            shoes = "Sandals"
        else:
            clothing = "Swim Suit"
            shoes = "Barefoot"

    elif time_of_day == "Evening" and temperature >= 10:
        clothing = "Shirt"
        shoes = "Moccasins"

    if temperature < 10:
        print("It's very cold, don't go outside!")
        exit()
else:
    print("Invalid Input!")
    exit()

# Print result
print(f"It's {temperature} degrees, get your {clothing} and {shoes}.")

