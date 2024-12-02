with open('lists.txt', 'r') as file:
    lines = file.readlines()

array1 = []
array2 = []

for line in lines:
    numbers = line.split()
    array1.append(int(numbers[0]))
    array2.append(int(numbers[1]))

array1.sort()
array2.sort()
deltas = [abs(array1[i]-array2[i]) for i in range(len(array1))]
print(sum(deltas))

counts = {}
for i in array2:
    counts[i] = counts.get(i, 0) + 1

simularity = [i*counts.get(i, 0) for i in array1]
print(sum(simularity))
