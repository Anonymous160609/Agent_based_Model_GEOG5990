import random

class Agent():
    def __init__ (self,_y,_x,environment,agents, colour):
        
        if (_y == None):
            self._y = random.randint(0,100)
        else:
            self._y =_y          
        if (_x == None):
            self._x = random.randint(0,100)
        else:
            self._x =_x 
        
        #self._y =_y          
        #self._x =_x 
        self.environment = environment
        self.agents = agents
        self.store = 0 #grass eaten 
        self.colour = colour
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
    
    def move(self):
        if self.colour != 'red':
            if random.random() < 0.5:
                self._y = (self._y + 1) % 100
            else: 
                self._y = (self._y - 1) % 100
                
            if random.random() < 0.5:
                self._x = (self._x + 1) % 100
            else: 
                self._x = (self._x - 1) % 100

    def eat(self): # can you make it eat what is left?
        if self.environment[self._x][self._y] > 10:
            self.environment[self._x][self._y] -= 10
            self.store += 10 
            
    #define distance function
    #This function takes in two arbitary agents 
    #(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
    #and will return the distance between them. 
    #for-each loop iterator, not index
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 

    def share_with_neighbours(self,neighbourhood):        
        for agent in self.agents:
            ########
                random.shuffle(self.agents)
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave)
                    
    def __str__(self):
        return str(self.store) and hex(id(self))
        return (hex(id(self))) 

        #return (str(self._y))
        #return str(self.store)


    
    
                 