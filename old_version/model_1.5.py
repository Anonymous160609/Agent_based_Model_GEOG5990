'''
Model:
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
'''


import random

# Set up variables.
y0 = 50
x0 = 50

# Random walk one step.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0,x0)

# Set up variables.
y1= 50
x1 = 50

# Random walk one step.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y0,x0)

#distance
distance = ((y0-y1)**2 + (x0-x1)**2)**0.5

