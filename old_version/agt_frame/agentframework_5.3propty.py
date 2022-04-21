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
    def __init__ (self):    
        self._y=random.randint(0,99)
        self._x=random.randint(0,99)
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "I am the 'x' property.")

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    def dely(self):
        del self._y
        
    y = property(gety, sety, dely, "I am the 'y' property.")

    #def randomize(self):
        #self.y=random.randint(0,99)
        #self.x=random.randint(0,99)


    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else: 
            self.y = (self.y - 1) % 100
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else: 
            self.x = (self.x - 1) % 100

    
    


    
'''
agents = []
agents.append(agentframework.Agent())

agents[i][0] 

agents[i][0] = (agents[i][0] + 1) % 100
agents[i].move()
matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
'''
    
                 