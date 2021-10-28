import math
import csv

with open('C:/Users/Meet Ankoliya/OneDrive/Desktop/Python/project-9/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

squares_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squares_list.append(a)

sum = 0
for i in squares_list:
    sum = sum + i

result = sum / (len(data)-1)

deviation = math.sqrt(result)
print(deviation)