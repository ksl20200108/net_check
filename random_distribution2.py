import random

distribution = []
point = 10
f = open('PDF2.txt', 'r')
distribution.append([0, 0])

for line in f:
    point = 1
    interval, probability = 0, 0

    for digit in line[:17]:
        if digit.isdigit():
            interval += (int(digit) / point)
            point *= 10
    point = 1

    for digit in line[18:]:
        if digit.isdigit():
            probability += (int(digit) / point)
            point *= 10

    distribution.append([interval, probability])

for i in range(1, len(distribution)):    # calculate cdf
    distribution[i] = [distribution[i][0], distribution[i][1]+distribution[i-1][1]]
    # print(distribution[i-1])

index1 = 0
random_number = random.uniform(0, distribution[len(distribution)-1][1])
for i in distribution:
    if random_number >= i[1]:
        index1 = distribution.index(i)
        break

result1 = random.uniform(distribution[index1-1][0], distribution[index1][0])
print("the result is :", result1)

# print(line[:17], "|| ", line[18:])
