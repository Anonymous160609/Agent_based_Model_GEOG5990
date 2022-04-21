'''
log: 
IndexError: list index out of range
#WRONG agent number is 99**n
#for i = 0 j = 0 at the start of the run, 
#the line sum += data[i-1][j] is trying to read into negative list space that doesn't exist
'''

# blur ---------------------------------------
import matplotlib.pyplot
import random

data = []
processed_data = []

# Fill with random data.


for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        datarow.append(random.randint(0,255))
    data.append(datarow)
    
len(datarow)
len(data)

# Blur.

'''
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
#WRONG agent number is 99**n
#for i = 0 j = 0 at the start of the run, 
#the line sum += data[i-1][j] is trying to read into negative list space that doesn't exist
'''
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
    datarow.append(sum)
    processed_data.append(datarow)

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()

# End ---------------------------------------