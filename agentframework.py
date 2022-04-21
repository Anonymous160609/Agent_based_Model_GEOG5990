import random

class Agent():
    """
    A class of sheep for ABM.
    
    Arguments:
    y: y coordinate of individual sheep in matplotlib
    x: x coordinate of individual sheep in matplotlib
    environment: environment of grassland for sheep to move and consume
    agents: list of all other sheep for interaction
    store: consumed grass by sheep
    colour: colour of sheep
    
    methods:
    .getx: print x value
    .setx: change x value
    .delx: delete x value
    .gety: print y value
    .sety: change y value
    move: randomly move sheep for integer distances in 2 directions out of four
    eat: consume the grass in environment, shift values from envirnment to .store 
    attribute
    distance_betwen: EuEuclidian distance between any 2 sheep
    share_with_neighbours: average all consumed grass by a number of sheep within
    a distance
    __str__: override .print method to get the .store value, rather than a momory
    location
    
    Returns:
    make encapsulated agents in ABM in main module.
    """
    def __init__ (self,_y,_x,environment,agents, colour):
        """
        >>>agent(1,1,1,1,1)
        <agentframework.Agent at 0x195a05d8340>
        
        initail attributes of Agent class
        
        Arguments:
        x: x coordinate, by default integer between (0,255)
        y: y coordinate, by default integer between (0,255)
        environment: environment of grassland for sheep to move and consume, a list
        agents: list of all other sheep for interaction, a 2-D list
        
        Returns:
        set up mandatory values to ABM to run
        """
        
        if (_y == None):
            self._y = random.randint(0,255)
        else:
            self._y =_y          
        if (_x == None):
            self._x = random.randint(0,255)
        else:
            self._x =_x 

        self.environment = environment
        self.agents = agents
        self.store = 0 #grass eaten 
        self.colour = colour
        
    def getx(self):
        """
        >>>agent = agentframwork.Agent(1,y,environment,agents,colour)
        >>>agent.getx
        1
        
        Print the vlaue of class attribute: x coordinate
        
        returns:
        the value of x
        """
        
        return self._x

    def setx(self, value):
        """
        >>>agent = agentframwork.Agent(1,y,environment,agents,colour)
        >>>agent.setx(2)
        >>>agent.getx
        2
        
        change the vlaue of class attribute: x coordinate
        
        returns:
        the value of input
        """
        self._x = value
        
    x = property(getx, setx, "I am the 'x' property.")

    def gety(self):
        """
        >>>agent = agentframwork.Agent(x,1,environment,agents,colour)
        >>>agent.gety
        1
        
        Print the vlaue of class attribute: y coordinate
        
        returns:
        the value of y
        """
        return self._y

    def sety(self, value):
        """
        >>>agent = agentframwork.Agent(x,1,environment,agents,colour)
        >>>agent.sety(2)
        >>>agent.gety
        2
        
        change the vlaue of class attribute: y coordinate
        
        returns:
        the value of input
        """
        
        self._y = value
        
    y = property(gety, sety, "I am the 'y' property.")
    
    def move(self):
        if self.colour != 'Red':
            if random.random() < 0.5:
                #self._y = (self._y + 1) % 100
                self._y = self._y + random.randint(1,10)
                if self._y > 254:
                    self._y = 254
            else: 
                #self._y = (self._y - 1) % 100
                self._y = self._y - random.randint(1,10)
                if self._y < 1:
                    self._y = 1
                
            if random.random() < 0.5:
                #self._x = (self._x + 1) % 100
                self._x = self._x + random.randint(1,10)
                if self._x > 254:
                    self._x = 254
            else: 
                #self._x = (self._x - 1) % 100
                self._x = self._x - random.randint(1,10)
                if self._x < 1:
                    self._x = 1
        else: 
            self._y = self._y
            self._x = self._x


    def eat(self): # can you make it eat what is left?
        """
        >>>agent = agentframework.Agent(x,y,11,agents,colour)
        >>>agent.store = 0
        >>>agent.eat
        >>>agent.store
        10
        
        eat the grass from grassland, transmit value from environemnt attribute 
        to store attribute
        
        arguments:
        self.environment: a list of integer value
        self.store: an integer value to accumulate
        
        returns:
        transmit a value
        """
        if self.environment[self._x][self._y] > 10:
            self.environment[self._x][self._y] -= 10
            self.store += 10 
            
    #define distance function
    #This function takes in two arbitary agents 
    #(at the moment, two rows in our agents list $[[...],[...]]$, each containing two values), 
    #and will return the distance between them. 
    #for-each loop iterator, not index
    def distance_between(self, agent):
        """
        >>>agent1 = agentframework.Agent(1,1,environment,agents,colour)
        >>>agent2 = agentframework.Agent(2,2,environment,agent1,colour)
        >>>agent2.distance_bewteen(agent2)
        1.414
        
        return the Euclidian distance between class instance sheep and an object
        in its attribute of agents list
        
        arguments:
        agent: another class instacne of sheep, needs x and y attributes
        
        returns:
        an Euclidian distance
        """
        
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 

    def share_with_neighbours(self,neighbourhood):        
        for agent in self.agents:
                random.shuffle(self.agents)
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave)
                    
    def __str__(self):
        return str(self.store)
        #return str(self.store) and hex(id(self))

class Wolf():
    """
    A class of wolf for ABM.
    
    Arguments:
    y: y coordinate of individual wolf in matplotlib
    x: x coordinate of individual wolf in matplotlib
    colour: colour of wolf
    
    methods:
    .getx: print x value
    .setx: change x value
    .delx: delete x value
    .gety: print y value
    .sety: change y value
    .dely: delete y value
    move: randomly move wolf for integer distances in 2 directions out of four

    Returns:
    make encapsulated wolf agent in ABM in main module.
    """
    def __init__ (self,_y,_x,colour):
        """
        >>>agent(1,1,1,1,1)
        <agentframework.Agent at 0x195a05d8340>
        
        initail attributes of Wolf class
        
        Arguments:
        x: x coordinate, by default integer between (0,255)
        y: y coordinate, by default integer between (0,255)
        colour: colour of wolf, text string in matplotlib colour list
        
        Returns:
        set up mandatory values to ABM to run
        """
        self._y = _y
        self._x = _x
        self.colour = colour
#def __init__ (self,_y,_x,colour,_acc_y,_acc_x):
#        self._acc_y = _acc_y
#        self._acc_x = _acc_y
        
    def getx(self):
        """
        >>>agent = agentframwork.Wolf(1,y,colour)
        >>>agent.getx
        1
        
        Print the vlaue of class attribute: x coordinate
        
        returns:
        the value of x
        """
        return self._x

    def setx(self, value):
        """
        >>>agent = agentframwork.Wolf(1,y,colour)
        >>>agent.setx(2)
        >>>agent.x
        2
        
        Change the vlaue of class attribute x to input 
        
        returns:
        the value of input
        """
        self._x = value
        
    x = property(getx, setx, "I am the 'x' property.")

    def gety(self):
        """
        >>>agent = agentframwork.Wolf(x,1,colour)
        >>>agent.gety
        1
        
        Print the vlaue of class attribute: y coordinate
        
        returns:
        the value of y
        """
        return self._y

    def sety(self, value):
        """
        >>>agent = agentframwork.Wolf(x,1,colour)
        >>>agent.sety(2)
        >>>agent.y
        2
        
        Change the vlaue of class attribute y to input 
        
        returns:
        the value of input
        """
        self._y = value
        
    y = property(gety, sety, "I am the 'y' property.")
    
    def move(self):
        if random.random() > 0.5:
            self._y = (self._y + 1) % 100
        else: 
            self._y = (self._y - 1) % 100
        if random.random() > 0.5:
            self._x = (self._x + 1) % 100
        else: 
            self._x = (self._x - 1) % 100

    #def move(self):
        #if self._acc_y > 0.5:
            #self._y = (self._y + 1) % 100
        #else: 
            #self._y = (self._y - 1) % 100
        #if self._acc_x > 0.5:
            #self._x = (self._x + 1) % 100
        #else: 
            #self._x = (self._x - 1) % 100
        #self._acc_y = random.randint(0,1)
        #self._acc_x = random.randint(0,1)    
    
                 