1. Content:
|
|__model.py
|__agentframework.py
|__webscrewler.py
|__environment.py
|__in.text
|__old_version

model.py 
THE FILE SHOULD BE RUN BY USER, it is the main script to run ABM, 
it generates an UI for ABM display and parameter user-inputs.

agentframework.py 
is the module of agents and methods used in ABM.

webscrewler.py 
gets coordinate values from html <tags> on:
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html,
and write into the in.text file.

environment.py 
turns the format of coordinate data into comma seperated values for model.py to read-in in in.txt. 

in.text 
stores environment values from <tags> on: 
https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html

old_version
contains outdated versions of this ABM software.

2. this ABM software:

It is an agent-based model with animation, statistic displays, and UI of parameter settings. 
It simulates the interaction of sheep, wolf, and grassland for a duration.
Sheep and wolf can move around grassland. Sheep can consume and store grass, 
can also average their grass sotre with nearly individuals.
Wolf can prey sheep, turn their colour into red, and stop sheep moving. 

3. Operation:

This ABM software should run in anaconda through spyder, 
but users can try running though other measures, 
provded including all required python packages. 
Initializing the model.py in spyder, it will show its UI. 
Users can input parameters in the left panel then confirm through button, 
else click "run" to start with initial parameters.
When it runs, it is expected to show interactions between sheep wolf grassland, 
and changes grassland, grass, and sheep corps by users,
both in form of animation and statistics.

4. Testing in final code:

In model.py, there are 4 testings. 
I - "importlib.reload(agentframework)" testing changes in class attributes and methods.
II - 2nd one is "#print(td_ys)  #print(td_xs)" testing results from html.
III - 4th one is Boolian conditioning clauses in "confirm" testing and correcting problematic parameters from user input.

In agentframework.py there are ??? testings.
I - doctest in "__init__" class method of "Agent" and "Wolf" testing passing of class attribute.
II - doctest in "getx/setx/gety/sety" meothds of class "Agent" and "Wolf", testing the storing of attributes.



5. Further Development: 

The statsictic display in this ABM is rather simple, users are encouraged to 
improve it to data visaulizations in bar chart animations etc. 
The basic movemnet function is based on global 2-d coordinates and randomizations in 4 directions.
Users could change these to angels, velocities, and accelarations.
Last but not leaset, it is expected to be an ecological model similiar to those on Netlogo, users
can write methods of grassland environment to change its growth as grass values over time, in responding to 
sheep and wolf interactions.
More realistic movement of wolf.

6. Issue:
The moving speed or displays in animation of sheep seem to inversely related to the number of sheep.
No infomative of parameter setting, if clicking run without confirm.
Reporting on excuting time is chaotic.
