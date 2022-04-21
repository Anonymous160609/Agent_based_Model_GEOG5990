import random
import operator 
import matplotlib.pyplot
import csv
import time
import matplotlib.pyplot
import matplotlib.animation 
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
    
#agents scales 
num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

#make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random.randint(0,99),random.randint(0,99),environment,agents))

#function that animates agents for "certain" times
def update(frame_number):
    fig.clear() 
    global carry_on
    for j in range(num_of_iterations):
        for i in range(num_of_agents): 
            if random.random() < 0.5:
                agents[i].move   
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)  
   
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)    
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
            
#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function,repeat=False)
matplotlib.pyplot.show() 

end = time.process_time()
print("time = " + str(end - start))


