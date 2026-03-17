 # --First way--:
# tail = input()
# body = input()
# head = input()
#
# animal = [head, body, tail]
#
# print(animal)


tail = input()
body = input()
head = input()

animal = [tail, body, head]
# --Second way--
# temp = animal[0]
#
# animal[0] = animal[2]
# animal[2] = temp

# --Third way--
animal[0], animal[2] = animal[2], animal[0]

print(animal)