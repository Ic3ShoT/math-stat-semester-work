import csv
import pandas
import matplotlib
import scipy
import plot
array_iris=[]
with open('iris.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            print(", ".join(row))
            array_iris.append(row)
i=0
first_column=[]
for i in range(0,30):
    first_column.append(float((array_iris[i])[0]))
    i=i+1
first_column_max=first_column[0]
for chislo in first_column:
    if chislo>first_column_max:
        first_column_max=chislo
print(first_column)
print(first_column_max)