'''
log: 
delete all the code dealing with the original second agent's coordinates, we no longer need it.
agents wandered off the edge
significantly shortened

Model:
# import random etc.
# Make y and x between [0,99]
# Move randomly
# answer = Pythagorian distance 
'''

import random
import operator 
import matplotlib.pyplot
import time

start = time.process_time()

#define distance function, returns NoneType
#This function takes in two arbitary agents 
#(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
#and will return the distance between them. 
def distance_between(agents_row_a, agents_row_b): 
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    #answer = (((agents[i][0] - agents[i][0])**2) + ((agents[i][1] - agents[i][1])**2))**0.5
    return(float(answer)) 
    
#make agents    
num_of_agents = 100
num_of_iterations = 100
agents = []

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#move agents for "certain" times
#Torus: % gives the remainder of a division
for i in range(num_of_agents):
    for j in range(num_of_iterations):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100

#agent disatnce
distance = distance_between(agents[9], agents[1])  

dist_list = []
#for i in range(agents):
for i in range(len(agents)):
    dist_ram = []
    for k in range(len(agents)):
        distance =  distance_between(agents[i], agents[k])   
        if distance == 0:
            dist_ram = dist_ram
        else: 
            dist_ram.append(distance)
            dist_list.append(dist_ram)
        
#print(max(dist_list))
print("max distance= " + str(max(max(dist_list))))
print("min distance= " + str(min(min(dist_list))))

#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() 

end = time.process_time()

print("time = " + str(end - start))

