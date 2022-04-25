import csv
import pandas
import matplotlib
import scipy
import plot

with open('iris.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            print(", ".join(row))