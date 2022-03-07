import random
import operator 
import matplotlib.pyplot
import csv
import time
import agentframework
import importlib
importlib.reload(agentframework)

start = time.process_time()

#read txt as 2d list via csv
environment = []
coords = open('in.txt', newline='') 
dataset = csv.reader(coords, quoting=csv.QUOTE_NONNUMERIC) 
for row in dataset:
    rowlist = []
    #environment.append(rowlist)
    for value in row:
        #rowlist = []
        rowlist.append(value)
    environment.append(rowlist) 
    
#plot environment 
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 

#define distance function
#This function takes in two arbitary agents 
#(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
#and will return the distance between them. 
#for-each loop iterator, not index
def distance_between(agents_row_a, agents_row_b): 
    return (((agents_row_a._x - agents_row_b._x)**2) +
   ((agents_row_a._y - agents_row_b._y)**2))**0.5
    
#agents scales 
num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

#make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random.randint(0,99),random.randint(0,99),environment,agents))

#move agents for "certain" times
for j in range(num_of_iterations):
    for i in range(num_of_agents):    
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)         
        
#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show() 

end = time.process_time()
print("time = " + str(end - start))

