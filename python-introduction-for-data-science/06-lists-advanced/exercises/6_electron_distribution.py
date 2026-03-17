#Read user input
electrons = int(input())

#Logic
n = 1
filled_shells = []

while electrons > 0:
    capacity = 2 * n ** 2
    if capacity <= electrons:
        filled_shells.append(capacity)
        electrons -= capacity
    else:
        filled_shells.append(electrons)
        electrons = 0
    n += 1

#Print output
print(filled_shells)


"""
6.	Electron Distribution
You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
•	The maximum number of electrons in a shell can be 2n**2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*3**2 = 18.
•	You should start filling the shells from the first one at the first position.
•	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
In the end, print a list with the filled shells.
Input	Output
10	    [2, 8]
44	    [2, 8, 18, 16]

Разсъждение за примерите:

Пример 1: Вход 10
1-ва обвивка: макс 2 електрона → запълваме 2, остават 8.
2-ра обвивка: макс 8 електрона → запълваме 8, остават 0.
Резултат: [2, 8]

Пример 2: Вход 44
1-ва: макс 2 → запълваме 2, остават 42.
2-ра: макс 8 → запълваме 8, остават 34.
3-та: макс 18 → запълваме 18, остават 16.
4-та: макс 32 → но останалите са 16, така че запълваме с останалите 16.
Резултат: [2, 8, 18, 16]

Изискването е:

Започни от първата обвивка (n=1, максимум 2n²).
Спри, когато не останат електрони.

"""