import csv

# reads the gme csv into a matrix
with open('gme.csv') as file:
    reader = csv.reader(file)
    gme = list(reader)

