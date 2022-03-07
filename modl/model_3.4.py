'''
log: 
delete all the code dealing with the original second agent's coordinates, we no longer need it.
agents wandered off the edge

Model:
# import random

# Make y and x between [0,99]

# Moverandomly

# answer = Pythagorian distance 

# print answer 
'''

import random
import operator 
import matplotlib.pyplot

num_of_agents = 10 
num_of_iterations = 100

'''
# Set up variables.
y0 = random.randint(0,99)
x0 = random.randint(0,99)
'''

agents = []

'''
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,100),random.randint(0,100)]) 
'''

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    
print(agents)
print(agents[0][1])

#move agents for "certain" times

'''
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
'''
   
''' 
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][0] += 1
    else: 
        agents[i][0] -= 1      
        
    if random.random() < 0.5:
        agents[i][1] += 1
    else: 
        agents[i][1] -= 1
'''

for i in range(num_of_agents):
    for j in range(num_of_iterations):
        if random.random() < 0.5:
            agents[i][0] += 1
        else: 
            agents[i][0] -= 1      
            
        if random.random() < 0.5:
            agents[i][1] += 1
        else: 
            agents[i][1] -= 1
#In general, in ABM, all agents move one step at a time, 
#rather than one agent moving a large number of steps, and then the next. 
        

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

print(max(agents))
print(max(agents, key=operator.itemgetter(1)))
#operator.itemgetter(1) gets the second element 

'''
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()
'''

'''
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
'''

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() 
#dots missiing 

'''
#test
y0 = 0
x0 = 0
y1 = 4
x1 = 3
'''

'''
#distance
distance = ((y0-y1)**2 + (x0-x1)**2)**0.5
print(distance)
'''
