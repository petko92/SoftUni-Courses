#Read user input
n = int(input())

#Logic
positives = []
negatives = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

negative_sum = 0
for i in range(len(negatives)):
    negative_sum += negatives[i]

#Print result
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {negative_sum}")
# print(f"Sum of negatives: {sum(negatives)}")