#Read user input
factor = int(input())
count = int(input())

#Logic
length = factor * count
my_list = []

for i in range(factor, length+1, factor):
        my_list.append(i)

#Print result
print(my_list)



"""
2.	Multiples List
Write a program that receives two numbers (factor and count). 
It should create a list with a length of the given count that contains only integer numbers,
 which are multiples of the given factor. The numbers should be only positive,
and they should be arranged in ascending order, starting from the value of the factor.

Example
Input	         Output
2
5             [2, 4, 6, 8, 10]
	        
1
10	         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""