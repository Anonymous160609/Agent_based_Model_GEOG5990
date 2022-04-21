'''
Model:
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
'''


import random

y0 = 50
x0 = 50

if random.random() < 0.5:
     y0 = y0 + 1
else:
     y0 = y0 - 1