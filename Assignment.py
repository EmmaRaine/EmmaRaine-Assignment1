# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:06:36 2021

@author: andre
"""

# Import the relevant packages from the python library.

# Import matplotlib which should import a library for creating static, animated, and interactive visualisations in the model. 

import matplotlib as mpl

# The following code sets up the matplotlib environment in tkinter to render the model to a tkinter canvas. 

mpl.use('TkAgg')

# Import the tkinter package from the python library to access the graphical user interface (GUI) module for Python

import tkinter 

# Import random should import the random module, which will allow the random functions within this module to be utilised.

import random 

# Import operator should import the operator module, which will allow a set of efficient fucntions, corresponding to
# intrinsic operators of python, to be utilised.

import operator 

# Import the matplotlib.pyplot module, which will allow a set of data to be inputted as graphs. This will be imported as plt 
# to reduce complexity and allow this module to be reffered to as plt throughout. 

import matplotlib.pyplot as plt

# Import the matplotlib.animation module, which will allow animated/live charts to be created.

import matplotlib.animation as anim

# Import the agentframeworkassignment file, created as a python file, in order to be able to utilise the code within that file
# in this model. This will be imported as af to minimise the risk of error throughout the work.

import agentframeworkassignment as af

# Import csv library from the python library to be able to parse or work with CSV files. 

import csv 

# Import the time library which allows access to modules and functions that in some way represent time in the code.

import time 

# Import the requests library which should allow HTTP requests to be made which reduces complexities behind the interface.

import requests

# Import the bs4 library to enable data to be pulled from HTML and XML files. This makes it easy to scrape information from web pages,
# providing idioms for iterating, searching, and modifying the parse tree, saving the user time. 

import bs4

# The following code creates a new variable (r) which accesses data from the web. This scrapes the HTTP data, downloading and printing
# x and y variables associated with this webpage. 

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# The following line of code indicates where to begin timing how long the code will take to run

start = time.time()

# The following code sets a new variable (f) which opens the CSV file. 

f = open('in.txt', newline='')

# The following code sets a new variable (reader) which reads the csv file into the model. 

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Create an empty list called 'environment' to shift the CSV file data into a list, which will hold the environmental data.

environment = []

# Make a new list (rowlist) before each row is processed, append the values in each row to the rowlist, and then append the rowlist to 
# the environment list.

for row in reader:
   rowlist = []
   for value in row:
       rowlist.append(value)
   environment.append(rowlist)

# The following block of code tests to above code to ensure the data has been properly appened to the environment list. 

# Print first value in environment list

print(environment[0][0])

# Assess how long the environment list is

nrows = len(environment)
ncols = len(environment[0])

# Print the lengths of the rows and columns in the environment list

print("nrows", nrows)
print(ncols)

# Print the last value in the environment list

print(environment[nrows-1][ncols-1])

# Plot the environment data using the plt module.
 
plt.imshow(environment)
plt.show()

# Create a function that will take in two arbitary agents. This code should return the straight-line/euclidean distance between all of
# these agents, derived from the af file, using pythagoras theorem.

#def distance_between(agents_row_a, agents_row_b):
    #return (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5
    
# Create an empty list called 'agents' which a set of coordinates can then be added to

agents = []

# Create a new variable (num_of_agents) to assign how many agents there will be. 

num_of_agents = 10

# Create a new variable (num_of_iterations) to move the agent coordinates an arbitary number of times. 

num_of_iterations = 100

# Create a new variable (num_of_steps) to set how many times agents will be run through loops.

num_of_steps = 50

# Create a new variable (neighbourhood) to allow agents to search for close neighbours within the distance attached to this variable (20).

neighbourhood = 20 

# To create a list of agent coordinates, obtained from a random location within the af file, the following code will create a for-loop 
# (for i in range), using the num_of_agents variable to determine the number of coordinates in the list.

# The code will use the agents.append function to add these sets of coordinates to the empty agents list. At this point the 
# environment list is passed into the agent constructor, along with the x and y variables.

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(af.Agent(environment, agents, y, x))

# The following code makes a single agent, connecting the agentframeworkassignment file with this model.

a = af.Agent(environment, agents, y, x)

# Define figure size and axes which, later in the model, should set figure parameters for plotting data. 
 
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# The following code prints the x and y variables defined within the af file to ensure the files are properly connected

print(a._y, a._x)

# Test that the self.x and self.y variables move randomly, in the way set out in the af file

a.move()
print(a._y, a._x)

# Test the eat() method defined in the af file to ensure it links properly to this model.

a.eat()
print(a._y, a._x)


# The following line of code creates a global variable (carry_on) that can be utilised both inside and outside functions

carry_on = True

# The following block of code creates a new function (update) that gives the model some behvaiour by randomly altering the self.x and 
# self.y coordinates using the move(), eat() and share_with_neighbours() methods defined in the af file, as long as the carry_on variable
# is True.
# Here, the y-coordinate will be referred to as agents[i]._y and the x-coordinate will be referred to as agents[i]._x as each agent 
# can be referred to, simply, as agents[i].

# To reduce model artifacts (patterns or errors in the way the model runs), this code uses the random.shuffle() function to randomise 
# the order in which agents are processed each iteration

# Using the code 'for j in range' specifies the number of times the agents will be run through the loops every time the update function 
# is run; here, this will be moved 10 times, as determined by num_of_steps.
# By adding the first for-loop (for i in range), the set of control statements can be executed once for each of the agents in the list.

def update(frame_number):
    global carry_on 
    fig.clear()   
    if True:
        random.shuffle (agents)
        for j in range(num_of_steps):
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)
                
                
# This second for-loop creates a new variable within the function, setting the agent_count of each agent to zero, still within the update
# function. 
               
            for i in range(num_of_agents):
                agent_count = 0
                
# Within this loop, the code that follows uses if statements, containing a block of code that evaluates a condition. 
# This checks the agent store of each agent and if the agent store exceeds 50, the agent_count variable increases by 1. Additionally, 
# if the agent_count variable is equal to the num_of_agents then the global carry_on variable becomes false, which prints a 
# stopping condition to stop the model running. 

                if agents[i].store > 50:
                        agent_count += 1
                if (agent_count == num_of_agents):
                    carry_on = False
                    print("stopping condition")
                
# The following code will use the matplotlib.pyplot function (imported as plt) to plot the environment data, along with the location of 
# each agent (using for i in range) as a scatter graph, still inside the update function. If statements determine the color of agents
# dependent on their stores. Agents with stores less than 12000 should be red, agents with stores greater than 12000 should be blue.

    plt.ylim(0, 100)
    plt.xlim(0, 100)
    plt.imshow(environment)
    for i in range(num_of_agents):
        if agents[i].store < 15000:
            plt.scatter(agents[i]._x,agents[i]._y, color='blue')
        if agents[i].store > 15000:
            plt.scatter(agents[i]._x,agents[i]._y, color='red')
    
        
                    
# Print the first set of agents in the list to ensure everything is working as it should be

print (agents[i]._y, agents[i]._x)                     

# The following code creates a generator function that allows the stopping condition to be met

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and awaits next call.
        a += 1               
        
# The following code creates a function to run an animation. This uses the FuncAnimation function in the animation module to create an 
# animation by repeatedly calling upon the update function. This uses the generator function to pass data in each frame of the animation. 
# canvas.draw() from the tkinter function to draw this animation within the canvas. The animation should stop running when the sequence 
# of frames is complete as repeat is set to False. 

def run():
    animation = anim.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# The following code builds the main GUI window by creating a new variable: root. This is given a title, then creates and lays out 
# a matplotlib canvas to be embedded within the GUI window, associated with figure parameters set out earlier in the model.

root = tkinter.Tk()
root.wm_title("Model")
canvas = mpl.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# This next section of code creates a menu for the GUI window and associates this with the run function which will allow the GUI to
# run the animation

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


# The following line of code indicates the end of the section of code in which time to run is being calculated.

end = time.time()

# The following code prints the time it takes (in seconds) for code to run between the start and end variables

print("time = " + str(end - start))

# This final line of code sets the GUI waiting for events and should allow the GUI to run the model effectively. 

tkinter.mainloop()




