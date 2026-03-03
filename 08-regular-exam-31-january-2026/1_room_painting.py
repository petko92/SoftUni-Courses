import math

count_of_cans_paint = int(input())
count_of_wallpaper_rows = int(input())
price_of_pair_glove = float(input())
price_for_one_brush = float(input())

price_for_paint = count_of_cans_paint * 21.50
price_for_wallpapers = count_of_wallpaper_rows * 5.20
gloves = math.ceil(count_of_wallpaper_rows * .35)
brushes = math.floor(count_of_cans_paint * .48)
price_for_gloves = gloves * price_of_pair_glove
price_for_brushes = brushes * price_for_one_brush

total_price_products = price_for_paint + price_for_wallpapers + price_for_gloves + price_for_brushes
delivery_price = total_price_products / 15
print(f"This delivery will cost {delivery_price:.2f} lv." )

'''
Comments
Total price for paint: 21.50 * 10 = 215 lv.
Total price for wallpapers: 5.20 * 8 = 41.60 lv.
Count needed gloves: 35% from 8 = 3 (2.8, rounded up)
Count needed brushes: 48% from 10 = 4 (4.8, rounded down) 
Total price for gloves: 3 * 2.2 = 6.60 lv.
Total price for brushes: 4 * 5 = 20 lv.
Total price for all products: 215 + 41.60 + 6.60 +  20 = 283.20 lv.
Delivery price: 1 / 15 from 283.20 = 18.88 lv.

'''


'''

Малък екип от хора има задачата да пребоядисат голяма стая. За да постигнат това, те се нуждаят от боя, тапети, ръкавици и четки, които ще поръчат онлайн.
Боята се продава в кутии, докато тапетите се предлагат на ролки. Известно е, че цената на една кутия боя е 21,50 лева, а цената на една ролка тапет е 5,20 лева.
Броят на необходимите ръкавици е 35% от броя на ролките тапети, закръглено нагоре, докато броят на необходимите четки е 48% от броя на кутиите боя, закръглено надолу.
 Вашата задача е да изчислите цената за доставка на всички необходими продукти, която е 1/15 от общата цена на продуктите.

Вход
От конзолата трябва да прочетете 4 числа:

1. Брой кутии с боя – цяло число в интервала [1 … 10 000]
2. Брой ролки тапети – цяло число в интервала [1 ... 10 000]
3. Цена за един чифт ръкавици – число с плаваща запетая в интервала [0.00 ... 1000.00]
4. Цена за една четка – число с плаваща запетая в интервала [0.00 ... 2000.00]
'''

'''
. Room Painting
A small team of people has the task of repainting a large room. To achieve this, they need paint, wallpaper, gloves, and brushes, which they will order online.
The paint is sold in cans, while the wallpaper comes in rolls. It is known that the price of one can of paint is 21.50 leva, and the price of one roll of wallpaper is 5.20 leva.
The number of required gloves is 35% of the number of wallpaper rolls, rounded up, while the number of required brushes is 48% of the number of paint cans, rounded down.
Your task is to calculate the delivery cost of all the necessary products, which is 1 / 15 of the total price of the products.

Input
From the console you must read 4 numbers:

1.	Count of the cans of paint – integer number in the interval [1 … 10 000]
2.	Count of the wallpaper rolls – integer number in the interval [1 ... 10 000]
3.	Price for one pair glove – floating-point number in the interval [0.00 ... 1000.00]
4.	Price for one brush – floating-point number in the interval [0.00 ... 2000.00]

Output
On the console you must print:

•	"This delivery will cost {delivery price} lv." 

The delivery price must be formatted to the second decimal digit.

'''