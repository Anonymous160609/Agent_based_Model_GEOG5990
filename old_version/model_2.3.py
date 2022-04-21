'''
Model:
# import random

# Make y0 and x0 between [0,99]

# Move y0 randomly

# Move x0 randomly

# Move y0 randomly

# Move x0 randomly

# Make y1 and x1 between [0,99]

# Move y1 randomly

# Move x1 randomly

# Move y1 randomly

# Move x1 randomly

# answer = Pythagorian distance between y0,x0 and y1,x1

# print answer 
'''

import random


'''
# Set up variables.
y0 = random.randint(0,99)
x0 = random.randint(0,99)
'''

agents = []
agents.append([random.randint(0,99),random.randint(0,99)]) 
print(agents)
print(agents[0][1])

'''
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
'''

# Set up variables.
y1= random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y1,x1])

'''
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
'''

'''
#test
y0 = 0
x0 = 0
y1 = 4
x1 = 3
'''

#distance
distance = ((y0-y1)**2 + (x0-x1)**2)**0.5
print(distance)
