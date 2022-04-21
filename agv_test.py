# Agent-based Model for sheep and wolf agents.
# Author: Anonymous0609(Github).
# Version: 10.3.


# 1. 
# Environemnts for ABM

import requests  # webscrewler for initial coordinates of agents
import bs4  # structuralize the screwlered for use
import tkinter  # indepedent interface for parameter input/output and ABM animation
#import matplotlib.pyplot  # also needs .animation
import matplotlib  # plots environment and agents via .pyplot, and make animation in tkinter interface via .animation 
matplotlib.use('TkAgg') #???
import random  # backup option for init agent coordinates & standardize the model
#import operator  # ???
#import sys  # for prompt interaction with parameters,dismissed due to UI input
import csv  # read in environment, also write out consumed environment
import time#timing the codes
import agentframework#agent class encasulated
from environment import environment
import importlib  # reload agentframework after adjustment
importlib.reload(agentframework)  # reload agentframework after adjustment


# 2. 
# Webscrewler for initial coordinates of agents.
# 100 groups of coordinates, thus the number of agents should smaller than 100.

# r is the object from url
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text  # convert r text data
# .BeautifulSoup reads useful info from html structure
soup = bs4.BeautifulSoup(content, 'html.parser')  
# make all values in <y> tag into list
td_ys = soup.find_all(attrs={"class" : "y"})  
# make all values in <x> tag into list
td_xs = soup.find_all(attrs={"class" : "x"})
# test td_ys and td_xs sturcture
#print(td_ys)  
#print(td_xs)

# old appraoch reads txt as 2d list via csv
# dismissed for webscrewler
#environment = []
#coords = open('in.txt', newline='') 
#dataset = csv.reader(coords, quoting=csv.QUOTE_NONNUMERIC) 
#for row in dataset:
#    rowlist = []
#    for value in row:
#        rowlist.append(value)
#    environment.append(rowlist)    


# 3.
# ABM Parameters.

# 3.1.   
# agents scales 
num_of_agents = 50
num_of_iterations = 50
chance_of_stop = 0.1

# 3.2.
# lists for sheep and wolf agents
agents = []
wolf = []

# 3.3.
# radious for sheep to interact
neighbourhood = 20
preyradious = 5
#colours of sheep and wolf agents
colours = []  # sheep colours
colours.append('White')
colours.append('Black')
colours.append('Brown')
colr = ('Blue')  # wolf colour
corp = ('Red')  # sheep corps colour

# 3.4.
# grass consumed by sheeps, for monitering ABM in tkinter
grass = 0
corps = 0

# 3.5. 
# like a switch of the ABM, ABM stops if it is turned to "False"
carry_on = True	
# timing for code excution
start_time = 0.0     
stop_time = 0.0

# 3.6.
# a medium containing the environment (and all agents) of ABM in tkinter interface 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
# polerize the coordinate directions, as left-to-right, down-to-up
ax = fig.add_axes([0, 0, 1, 1])  

# Old parameter inputs from prompt by users, 
# via positioned parameters in a function. 
#num_of_agents = sys.argv[1]
#num_of_iterations = sys.argv[2]
#neighbourhood =sys.argv[3]

# 4. 
# Agents creation.

# Use coordinates from Section 2. into agent classes from agentframework.py.
# make sheep
for i in range(num_of_agents):
    # turns text strings into integer numbers
    y = int(td_ys[i].text)  
    x = int(td_xs[i].text)
    # sequentially set sheep colours as 1. white, 2. black, 3. brown
    j = i%len(colours)
    # positionally pass to built-in attributes of sheep class 
    agents.append(agentframework.Agent(y,x,environment,agents,colours[j]))
# make wolf, positionally pass its random initial locations,
# to its built-in class attributes    
wolf.append(agentframework.Wolf(0,0,colr))


# 5. 
# Callback functions.

# 5.1.
# ABM interaction functions.

def prey(sheep,wolf,distrance):
    """
    >>>agents[1].setx(1)
    >>agents[1].sety(1)
    >>>wolf[0].setx(2)
    >>>wolf[0].sety(2)
    preyradious=5
    >>> prey(agents[1],wolf[0],preyradious)
    >>>agent[1].color
    'Red'
    
    Prey function between wolf class and sheep class.
    
    Keyword arguments: 
    a -- sheep
    b -- wolf
    distance --- Euclidian distance between sheep and wolf
    
    Returns:
    change of sheep color, pass to .move() method in class Sheep to stop sheep
    move
    """
    if (((sheep._x - wolf._x)**2) + ((sheep._y - wolf._y)**2))**0.5 < int(preyradious):
        sheep.colour = 'Red'

# Old function for wolf to hunt sheep, has accelerations for wolf's directions.
# Interaction is not obvious in rand.randint() based movements, 
# and absolute coordinates. Because wolf has higher change to 
# locate around border, and sheep as a whole always stay in centre.
# def drift(a,b):
#     if (((a._x - b._x)**2) + ((a._y - b._y)**2))**0.5 < 20:
#        if b._acc_y>0:
#            if a._y >b._y:
#                a._y = int(a._y)
#            else:
#               a._y = int(b._y - 2)        
#        if b._acc_y<0:
#            if a._y >b._y:
#                a._y = int(b._y - 2)
#            else:
#                a._y = int(a._y)                              
#        if b._acc_x>0:
#            if a._x >b._x:
#                a._y = int(a._x)
#           else:
#                a._x = int(b._x - 2)     
#        if b._acc_x<0:
#            if a._x >b._x:
#                a._x = int(a._x - 2)
#            else:
#                a._x = int(b._x)         
#        b._acc_y=random.randint(0,1)
#        b._acc_x=random.randint(0,1)

# 5.2. 
# Animation functions.

# Animation for sheep and wolf agents to move and intract,
# for "certain" times of "num_of_iteration".
def update(frame_number):  
    """   
    A list of interactions by agents:
    1. sheep eat grass
    2. sheep accumulates grass
    3. sheep share (bit funny) grass with nearby sheep
    5. wolf moves
    6. wolf eats sheep, eaten sheep turn into corps
    4. rest sheep move
    
    Keyword argument:
    fame_number -- each frame in animation in tkiner for ABM
      
    Returns:
    Changes in agents in environment in ABM in  tkinter.
    """
    
    # clean the ploted picture object from previous round of code
    fig.clear()   
    
    # localize global variables from section 4, 
    # for this update function to use and change 
    global carry_on
    global chance_of_stop
    global stop_time
    global grass
    global corps
    
    # 10% chances of stop in every iteration of agents interaction
    #if random.random() < 0.01:
    if random.random() < chance_of_stop:
        carry_on = False
        print("stopping condition,")
        print("excuting time:", (stop_time-start_time))
    
    # update interactions
    for i in range(num_of_agents):
        random.shuffle(agents)  # random sequence for sheep to move     
        agents[i].eat()  # built-in method of sheep class to eat grass
        grass += agents[i].store  # accumulates eaten grass to monite in tkinter
        agents[i].share_with_neighbours(neighbourhood)  # built-in method to share
        wolf[0].move()
        #drift(agents[i], sherphed[0])  # old hunt function dismissed
        prey(agents[i], wolf[0],preyradious)  # new hunt function
        corps = agents.count(agents[i].colour=='Red')  # count dead sheep
        agents[i].move()  # built-in method of sheep class to move

    # plot sheep and wolf agents on scale of 255^255, over environment
    matplotlib.pyplot.xlim(0, 255)
    matplotlib.pyplot.ylim(0, 255)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.scatter(wolf[0]._y,wolf[0]._x,color=wolf[0].colour)
    # colour sheep and wolf agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x,color=agents[i].colour)
    
    # timing the runing of code
    stop_time = time.process_time()
        
# Infomative function shows the reason of ABM's stop.     
def gen_function():
    """
    Boolian conditioning function to inform one cause of ABM's stop.
    
    Arguments:
    a: local variable of iterator, to iterate num_of_iterations
    num_of_iterations: passed global parameter deciding required run times of ABM
    

    Returns:
    Once the passed iteration number from parameter is exceeded,
    print informative text.
    """
    a = 0  # new iterator to num_of_iteration
    # golobal variable form 3.4., for condition clause next line
    global carry_on
    #if not exceeding iteration parameter, AND ABM still running
    while (a < num_of_iterations) & (carry_on) :
        # let ABM run this time, while increase a to exceed iteration number
        # eventually to stop ABM
        yield a
        a = a + 1
    #if carry_on is True: # bad grammatic in Python
    # if carry_on is true, BUT iteration number exceeded by a
    if carry_on:
        print("Iteration number exceed, stop")
        print("Excuting time:", (stop_time-start_time))

#Draw ABM 
def run():
    """ 
    On-click function to triggle ABM's running (then stopping).     

    Arguments: 
    animation: Make this ABM an istance based on previous functions in section 5.,
    and based on FuncAnimation method of matplotlib package, to display 
    changes in each iteration. Its sub-arguments: fig, update, 
    frames=gen_function, repeat=False (explianed in previous documentations, 
    also see documentation of matplotlib.animation.FuncAnimation)
    canvas.draw(): draw animation instacne on the graphic weidge of tkinter
    
    Returns: 
    display this ABM as graphics in tkinter
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #matplotlib.pyplot.show()  # old display solution involves no changes 
    # between agents and environment
    canvas.draw()  # draw ABM in tkinter

   
# 5.3.
# Parameter input function.

def confirm ():
    """
    On-click function to pass parameters from user inputs in tkinter UI to ABM.
    It also detects and changes error-causing parameters to appropriate values.
    
    Arguments:
    button_sheepnum.get(): get value from tkinter entry of sheep number parameter
    buttom_iterationnum.get(): get value from tkinter entry of iteration number 
    parameter
    button_random.get(): get value from tkinter entry of stopping chance in
    each iteration
    button_neighbournum.get(): get value from tkinter entry of sheep's radious 
    for sharing grass
    button_preyredious.get(): get value from tkinter entry of wolf's radious of 
    preying sheep
    
        
    Returns: 
    number_of_sheep = button_sheepnum.get(), in 3.1.
    number_of_iterations = buttom_iterationnum.get(), in 3.1.
    random.radom() < button_random.get(), in update() in 5.1.
    neighbourhood = button_neighbournum.get(), in 3.3.
    (((a._x - b._x)**2) + ((a._y - b._y)**2))**0.5 < button_preyredious.get(),
    in prey() in 5.1.
    
    """
    global start_time  # for timing the code
    start_time = time.process_time()  # to subtract in monitor in tkinter
    
    global num_of_agents  # for parameter passing
    if button_sheepnum.get():
        if int(button_sheepnum.get()) > int(num_of_agents):  #IndexError
            print("IndexError in line 147: sheep number out index, set to initial value")
            num_of_agents=num_of_agents
        elif int(button_sheepnum.get()) < 3:  # Error: sheep change(loop) their colours
            print("Wrong colour: sheep number below index, set to 3")
            num_of_agents=3    
        else:
            print("Sheep number pass succeed")
            num_of_agents = int(button_sheepnum.get())     
    else:
        print("No sheep number input, set to initial value")
        num_of_agents=num_of_agents
        
    global num_of_iterations
    
    if buttom_iterationnum.get():
        if int(buttom_iterationnum.get()) <= 1:
            print("Wrong value: no iterating, set to 1")
            num_of_iterations = 1
        else:
            print("Iteration number pass succeed")
            num_of_iterations = int(buttom_iterationnum.get())
    else:
        print("No iteration number input, set to initial value")
        num_of_iterations = 50
        
    global chance_of_stop
    
    if button_random.get():
        if float(button_random.get()) >= 1:
            print("Wrong value: chance meets 1, set to 0.9")
            chance_of_stop = 0.9
        elif float(button_random.get()) <= 0:
            print("Wrong value: chance meets 0, set to 0.1")
            chance_of_stop = 0.1
        else:
            print("Changce of stop pass succeed")
            chance_of_stop = float(str(button_random.get()))
    else:
        print("No chance input: set to initial value")
        chance_of_stop = chance_of_stop
        
    global neighbourhood
    
    if button_neighbournum.get():
        if int(button_neighbournum.get()) < 0:
            print("Wrong value: negative distance, set to 0")
            neighbourhood = 0
        else:
            print("Neighbourhood radious pass succeed")
            neighbourhood = int(button_neighbournum.get())
    else:
        print("No neighbourhood radious input, set to initial value")
        neighbourhood = neighbourhood
        
            
    global preyradious
        
    if button_preyredious.get():
        if int(button_neighbournum.get()) < 1:
            print("Wrong value: wof preys only overlapping with sheep, set to 1")
            preyradious = 1
        elif int(button_neighbournum.get()) > 50:
            print("Wrong value: this wolf seems is Fenrir consuming the whole world, set to 50")
            preyradious = 50
        else:
            print("Prey radious pass succeed")
            preyradious = preyradious
    else:
        print("No prey radious input, set to initial value")
        c = 5
            
        
# Old function in solving logical errors in parameter inputs,
# test: is less insufficient than if:, in lacking of condition clauses.
#def confirm ():
#    try: 
#        global num_of_agents
#        num_of_agents = int(button_sheepnum.get())
#    except AttributeError:
#        print("err of method(s) in tkinter widge , initiate failure")
#    except IndexError:
#        print("value > 50, out of index, set as 50")
#        num_of_agents = 50
#    else: 
#        print("parameter pass succeed")
 
# Old I/O bases on command prompt, replaced by tkinter UI I/O.
#print("sys.argv for python module name:", sys.argv[0])
#print("Argument List: 1.python module: 2.number_of_agents; number_of_iterations; radious_of_neighbourhood", str(sys.argv))
#print("Number of elements excluding the name of the program:",(len(sys.argv)-1))


# 6.
#Interface structures.    
root = tkinter.Tk() #TK interface called root, irrelavent to menu structure
root.title("ABM of wolf, sheep and consumings")

# 6.1. 
# left panel for parameter inputs
tkinter.Label(root,text="Sheep Number:",textvariable=num_of_agents).grid(row=0,column=0)
button_sheepnum = tkinter.Entry(root)
button_sheepnum.grid(row=1,column=0)
tkinter.Label(root,text="Iteration Number:").grid(row=2,column=0)
buttom_iterationnum = tkinter.Entry(root)
buttom_iterationnum.grid(row=3,column=0)
tkinter.Label(root,text="Chance of Stop in Iteration (float, (0,1)):").grid(row=4,column=0)
button_random = tkinter.Entry(root)
button_random.grid(row=5,column=0)
tkinter.Label(root,text="Neighbourhood Radious of Sheep:").grid(row=6,column=0)
button_neighbournum = tkinter.Entry(root)
button_neighbournum.grid(row=7,column=0)
tkinter.Label(root,text="Prey Radious of Wolf:").grid(row=8,column=0)
button_preyredious = tkinter.Entry(root)
button_preyredious.grid(row=9,column=0)
tkinter.Button(root,text="Confirm", command=confirm).grid(row=10,column=0)
tkinter.Button(root,text="Run",command=run).grid(row=11,column=0)

# 6.2. 
# middle panel for ABM graphics
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)  # .pack
#() is less toggable than .grid() in displaying
canvas._tkcanvas.grid(row=0,rowspan=12,column=1) 

# 6.3.
# right panel for variable monitorings
tkinter.Label(root,text="Grass Consumed:").grid(row=4,column=3)
grass_display = tkinter.Label(root,text=grass).grid(row=6,column=3)
tkinter.Label(root,text="Sheep Preyed:").grid(row=7,column=3)
corps_display = tkinter.Label(root,text=corps).grid(row=8,column=3)
# 6.
# to run tk window (Wait for interactions). 
root.mainloop() 

# 7.
# write out consumed environemnt(grassland) as csv file in model folder
with open('consumed_environment.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(environment)
