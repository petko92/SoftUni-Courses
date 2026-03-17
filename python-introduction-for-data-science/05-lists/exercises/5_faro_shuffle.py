#Read user input
cards = input().split()  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
shuffles = int(input())

#Logic
for _ in range(shuffles):
    half = len(cards) // 2
    first_half = cards[:half]
    second_half = cards[half:]

    result = []
    for i in range(half):
        result.append(first_half[i])
        result.append(second_half[i])

    cards = result
#Print result
print(cards)  # ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

"""
['ace', 'two', 'three', 'four', 'five', 'six']

['ace', 'four', 'two', 'five', 'three', 'six']

"""

"""
5.	Faro Shuffle
A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number.

"""

