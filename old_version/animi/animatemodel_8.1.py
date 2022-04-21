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
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show() 
    
#agents scales 
num_of_agents = 10
num_of_iterations = 40
agents = []
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random.randint(0,99),random.randint(0,99),environment,agents))

carry_on = True	

#animation for move agents for "certain" times
def update(frame_number):    
    fig.clear()   
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")

    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x)
            #print(agents[i]._y,agents[i]._x)
            
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
#plot agents
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()


