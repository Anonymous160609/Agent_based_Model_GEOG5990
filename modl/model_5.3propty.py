import random
import operator 
import matplotlib.pyplot
import time
import agentframework

start = time.process_time()

a = agentframework.Agent()
a.move()
print(a._y, a._x)

#define distance function
#This function takes in two arbitary agents 
#(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
#and will return the distance between them. 
#for-each loop iterator, not index
def distance_between(agents_row_a, agents_row_b): 
    return (((agents_row_a._x - agents_row_b._x)**2) +
   ((agents_row_a._y - agents_row_b._y)**2))**0.5
    '''
    return(float((((agents_row_a[0] - agents_row_b[0])**2) 
          + ((agents_row_a[1] - agents_row_b[1])**2))**0.5))
    '''
    
#agents scales 
num_of_agents = 10
num_of_iterations = 100
agents = []

#make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

#move agents for "certain" times
for j in range(num_of_iterations):
    for i in range(num_of_agents):    
        agents[i].move()

#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show() 

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 

end = time.process_time()
print("time = " + str(end - start))

