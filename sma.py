import csv
import numpy as np

# reads the gme csv into a matrix
with open('gme.csv') as file:
    reader = csv.reader(file)
    gme = list(reader)

del gme[0]
gme = list(reversed(gme))

# change the date of the csv, where the first number is the number of trading days since May 12th, 2021
for loop in range(len(gme)):
    gme[loop][0] = loop

sma = list()
for loop in range(len(gme) - 9):
    moving_day = 0
    average_sum = 0
    while moving_day < 10:
        average_sum += float(gme[loop + moving_day][1])
        moving_day += 1
    sma10 = average_sum / 10
    sma.append(sma10)

count = 9
with open('sma10.txt', 'w') as gme_new:
    for item in sma:
        gme_new.write(str(count) + '	' + str(item) + '\n')
        count += 1
