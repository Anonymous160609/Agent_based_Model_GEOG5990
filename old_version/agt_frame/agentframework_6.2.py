'''
#all object methods have to have a parameter label to assign to the object 
#when it is sent in; usually called self.
'''

###
#agents.append(agentframework.Agent())
'''
agents.append([random.randint(0,99),random.randint(0,99)])
'''

###
#agents[i].move()
'''
if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else: 
    agents[i][0] = (agents[i][0] - 1) % 100
    
if random.random() < 0.5:
    agents[i][1] = (agents[i][1] + 1) % 100
else: 
    agents[i][1] = (agents[i][1] - 1) % 100
'''

import random

class Agent():
    def __init__ (self,y,x,environment):          
        self.y=y
        self.x=x
        self.environment = environment
        self.store = 0 # We'll come to this in a second. 
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else: 
            self.y = (self.y - 1) % 100
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else: 
            self.x = (self.x - 1) % 100

    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
    


    
'''
agents = []
agents.append(agentframework.Agent())

agents[i][0] 

agents[i][0] = (agents[i][0] + 1) % 100
agents[i].move()
matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
'''
    
                 