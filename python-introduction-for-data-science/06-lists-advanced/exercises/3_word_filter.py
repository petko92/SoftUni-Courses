text = input().split(" ")
# for word in text:
#     if len(word) % 2 == 0:
#         print(word)
#
# even_words = list(filter(lambda w: len(w) % 2 == 0, text))
# print('\n'.join(even_word))

even_words = [word for word in text if len(word) % 2 == 0]
print('\n'.join(even_words))

# print('\n'.join(word for word in text if len(word) % 2 == 0))
"""
3.	Word Filter
Using comprehension, write a program that receives some text, separated by space, and takes only those words whose length is even.
Print each word on a new line.
Examples
Input	                     Output
kiwi orange banana apple	 kiwi
                             orange
                             banana

pizza cake pasta chips	     cake

"""