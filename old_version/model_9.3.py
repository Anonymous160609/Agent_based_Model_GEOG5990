import requests#webscrewler for initial coordinates of agents
import bs4#structuralize the screwlered for use
import tkinter#indepedent interface for animation
import matplotlib#plots environment and agents in tkinter interface 
matplotlib.use('TkAgg') #???
import random#backup for init agent coordinates & standardize the model
import operator#???
import matplotlib.pyplot#plots environment and agents in tkinter interface
import csv#read in environment
import time#timing the codes
import agentframework#agent class encasulated
from environment import environment
import importlib#reload agentframework after adjustment
importlib.reload(agentframework)#reload agentframework after adjustment

start = time.process_time()#start timing 

#webscrewler for initial coordinates of agents
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

'''
#read txt as 2d list via csv
environment = []
coords = open('in.txt', newline='') 
dataset = csv.reader(coords, quoting=csv.QUOTE_NONNUMERIC) 
for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)    
'''
    
#agents scales 
num_of_agents = 10
num_of_iterations = 40
agents = []
neighbourhood = 20
colours = []

#colours of agents
colours.append('White')
colours.append('Black')
colours.append('Brown')

#size of the tkinter interface 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#make agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    j = i%len(colours)
    print(j)
    agents.append(agentframework.Agent(y,x,environment,agents,colours[j]))

#???
carry_on = True	

#animation for move agents for "certain" times
def update(frame_number):    
    fig.clear()   
    for i in range(num_of_agents):
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
            
    if random.random() < 0.1:#10% chances of stop in every round of agent movement
        carry_on = False
        print("stopping condition")
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._y,agents[i]._x,color=agents[i].colour)

#???            
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a# Returns control and waits next call.
        a = a + 1

#plot agents
def run():        
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()
    canvas.draw()

#interface structures    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

#menu structures 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar) #submenu under root menu
menu_bar.add_cascade(label="Model", menu=model_menu) #add submenu to root menu
model_menu.add_command(label="Run model", command=run)  #command=run: run onclick "run model"

tkinter.mainloop() # Wait for interactions. 

print(agents[4])
agents[4]
