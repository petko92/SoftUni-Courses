# Read user input
deposited_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input()) / 100   #5.7% / 100 = 0.057

# Logic
amount = deposited_amount + term_of_deposit * (deposited_amount * annual_interest_rate) / 12

# Print result
print(amount)

