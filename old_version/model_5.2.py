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
###
import agentframework
start = time.process_time()
a = agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)

#define distance function, returns NoneType
#This function takes in two arbitary agents 
#(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
#and will return the distance between them. 
def distance_between(agents_row_a, agents_row_b): 
    ###
    #for-each loop iterator, not index
    return (((agents_row_a.x - agents_row_b.x)**2) +
   ((agents_row_a.y - agents_row_b.y)**2))**0.5
    '''
    return(float((((agents_row_a[0] - agents_row_b[0])**2) 
          + ((agents_row_a[1] - agents_row_b[1])**2))**0.5))
'''
    #answer = (((agents[i][0] - agents[i][0])**2) + ((agents[i][1] - agents[i][1])**2))**0.5
    
#agents scales 
num_of_agents = 10
num_of_iterations = 100
agents = []

#make agents
for i in range(num_of_agents):
    ###
    agents.append(agentframework.Agent())
    '''
    agents.append([random.randint(0,99),random.randint(0,99)])
    '''

#move agents for "certain" times
#Torus: % gives the remainder of a division
for j in range(num_of_iterations):
    for i in range(num_of_agents):    
        ###
        agents[i].move()
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100
        

'''
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
'''

#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    ###
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    '''
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    '''
matplotlib.pyplot.show() 

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 

end = time.process_time()
print("time = " + str(end - start))

