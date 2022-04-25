import csv
import pandas
import matplotlib
import scipy
import plot
#интервальный вариационный ряд
#выборочное среднее
#выборочная дисперсия
#выборочное отклонение
#мода
#медиана
#ассиметрия
#эксцесс
#доверительный интервал для генерального среднего
#доверительный интервал для генеральной дисперсии
#гистограмма

array_iris=[]
with open('iris.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            print(", ".join(row))
            array_iris.append(row)
i=0
first_column=[]
for i in range(0, 150):
    first_column.append(float((array_iris[i])[0]))
    i = i + 1
first_column_max = first_column[0]

def max(arr):
    first_column_max=arr[0]
    for chislo in arr:
        if chislo>first_column_max:
            first_column_max=chislo
    return first_column_max
print(max(first_column))