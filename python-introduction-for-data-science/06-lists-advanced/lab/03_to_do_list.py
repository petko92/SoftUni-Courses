to_do_list = ["" for i in range(10)]

while True:
    cmd = input()
    if cmd == "End":
        break
    importance, task = cmd.split("-")
    importance = int(importance) - 1
    to_do_list.pop(importance)
    to_do_list.insert(importance, task)
    # to_do_list[importance] = task

result = [x for x in to_do_list if x != ""]
print(result)

"""
3.	To-do List
You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.
Example
Input	                     Output
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End                       ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']

3-C
2-A
1-B
6-V
End	                     ['B', 'A', 'C', 'V']

"""