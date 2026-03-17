#Read user input
num = int(input())

#Logic
original_num = num  # Запазваме за изходните данни
is_special = True


while num > 0:
    digit = num % 10  # Вземаме последната цифра
    if digit == 0:
        num //= 10
        continue
    if original_num % digit != 0:
        is_special = False
        break
    num //= 10  # Премахваме последната цифра

#Print result
if is_special:
    print(f"{original_num} is special")
else:
    print(f"{original_num} is not special")