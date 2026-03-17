orders = {}

while True:
    user_input = input()
    if user_input == "buy":
        break

    product, price, quantity = user_input.split()
    if product not in orders:
        orders[product] = [float(price), int(quantity)]
    else:
        old_price, old_qty = orders[product]
        new_price = float(price)
        new_quantity = old_qty + int(quantity)
        orders[product] = [new_price, new_quantity]

#Extract data, Print output
for product, (price, quantity) in orders.items():
    total = price * quantity
    print(f"{product} -> {total:.2f}")

'''
5.	Orders
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
•	If the product doesn't exist yet, add it with its starting quantity.
•	If you receive a product, that already exists, increase its quantity by the input quantity and if its price is different, replace  the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items.
 Finally, print all items with their names and the total price of each product.
Input
•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
•	The product data is always delimited by a single space.
Output
•	Print information about each product in the following format:
"{product_name} -> {total_price}"
•	Format the total price to the 2nd digit after the decimal separator.
Examples
   Input	                  Output
Beer 2.20 100
IceTea 1.50 50
NukaCola 3.30 80
Water 1.00 500
buy	                    Beer -> 220.00
                        IceTea -> 75.00
                        NukaCola -> 264.00
                        Water -> 500.00
Beer 2.40 350
Water 1.25 200
IceTea 5.20 100
Beer 1.20 200
IceTea 0.50 120
buy	                     Beer -> 660.00
                         Water -> 250.00
                         IceTea -> 110.00
CesarSalad 10.20 25
SuperEnergy 0.80 400
Beer 1.35 350
IceCream 1.50 25
buy	                     CesarSalad -> 255.00
                         SuperEnergy -> 320.00
                         Beer -> 472.50
                         IceCream -> 37.50

'''

