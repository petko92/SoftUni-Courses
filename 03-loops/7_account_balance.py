#Read user input
money = input()

#Logic
incomes = 0
expenses = 0
balance = 0

while money != "End":
    amount = float(money)

    if amount < 0:
        expenses += abs(amount)
        print(f"Decrease: {abs(amount):.2f}")
    else:
        incomes += amount
        print(f"Increase: {amount:.2f}")

    money = input()

balance = incomes - expenses

#Print result
print(f"Balance: {balance:.2f}")


"""
7.	Account Balance
Write a program to calculate an account balance:
•	Read a sequence of incomes / expenses, until "End" is read
•	Add the money to the balance (starting form 0)
•	Print "Increase: {money}" or "Decrease: {money}", where value is formatted to the second decimal digit
•	Finally, print the account balance, formatted to the second decimal digit in the following format: "Balance: {account balance}"
Input
500
15.5
-80.35
End

Output
Increase: 500.00
Increase: 15.50
Decrease: -80.35
Balance: 435.15

"""