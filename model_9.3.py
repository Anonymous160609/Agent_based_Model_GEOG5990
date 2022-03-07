from webscrewler import cds
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
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
    y = cds[i][0]
    x = cds[i][1]
    agents.append(agentframework.Agent(y,x,environment,agents))

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
def run():        
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()
    canvas.draw()
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar) #submenu under root menu
menu_bar.add_cascade(label="Model", menu=model_menu) # add submenu to root menu
model_menu.add_command(label="Run model", command=run)  #command=run: run onclick "run model"

tkinter.mainloop() # Wait for interactions. 

