import csv

# reads the gme csv into a matrix
with open('gme.csv') as file:
    reader = csv.reader(file)
    gme = list(reader)

del gme[0]
gme = list(reversed(gme))

# change the date of the csv, where the first number is the number of trading days since May 12th, 2021
for loop in range(len(gme)):
    gme[loop][0] = loop

A = list()
for loop in range(len(gme)):
