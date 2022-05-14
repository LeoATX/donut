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

# y = C + Dx
# Ax = b
# x = (AᵀA)⁻¹ * Aᵀ * b


# linear and nonlinear regression
def regression(power: int):
    matrix_a = list()
    for row in range(len(gme)):
        # add a column of ones
        matrix_a.append([1])

    for row in range(len(gme)):
        for exponent in range(power):
            matrix_a[row].append((gme[row][0]) ** (exponent + 1))

    b = list()
    for row in range(len(gme)):
        b.append(float(gme[row][1]))

    # x = (AᵀA)⁻¹ * Aᵀ * b
    print(np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(matrix_a), matrix_a)), np.transpose(matrix_a)), b))


regression(0)
regression(1)
regression(2)
regression(3)
regression(4)
regression(5)
regression(8)
