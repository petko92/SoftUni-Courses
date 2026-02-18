sequence_of_numbers = input().split(', ')
numbers = list(map(int, sequence_of_numbers))

if not numbers:
    exit()

max_num = max(numbers)
group = 10

while group <= max_num + 9:  # +9 за да включим последната група ако max_num е точно кратно на 10
    current_group = []
    lower_bound = group - 10

    for num in len(numbers) // 2:
        if lower_bound < num <= group:
            current_group.append(num)

    #current_group = [num for num in numbers if lower_bound < num <= group]

    print(f"Group of {group}'s: {current_group}")
    group += 10


"""
7.	Group of 10's
Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.

Input	                             Output
8, 12, 38, 3, 17, 19, 25, 35, 50	Group of 10's: [8, 3]
                                    Group of 20's: [12, 17, 19]
                                    Group of 30's: [25]
                                    Group of 40's: [38, 35]
                                    Group of 50's: [50]

"""