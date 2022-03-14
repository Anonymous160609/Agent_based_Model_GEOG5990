import csv#read in environment

#read txt as 2d list via csv
environment = []
coords = open('in.txt', newline='') 
dataset = csv.reader(coords, quoting=csv.QUOTE_NONNUMERIC) 
for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)