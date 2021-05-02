# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:17:26 2021

@author: andre
"""
# Import the random module to allow random functions to be utilised within the code.

import random

# The following code sets up an agent class using the init method and defines x and y variables.
# All object methods require a parameter label to assign to the object; this is self label and essentially means that those 
# x and y values belong to that class.
# Here, all agents are linked to the environment object which means as the agents change the environment data, the environment is 
# changed for all of the agents.
# Created a link to get the list of agents into each of the agents

class Agent():
    def __init__(self, environment, agents, y=None, x=None):
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99)
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y


# The following code makes a move() method within the Agent class. The code will randomly alter the self.x and self.y coordinates using 
# control flow (if-else) statements. 

# The if statement contains a block of code that evaluates a condition and makes a choice. An else statement contains the block of code that 
# executes, if the condition in the if statement is not met.

# This code will generate a random floating number between 0 and 1 using the 
# random.random() function from the random module. The code should random walk the coordinates 1 step depending on which conditions are
# met; if random.random() is less than 0.5 self.x/self.y coordinates will increase by 1 and if random.random() is greater than 0.5
# self.x/self.y coordiantes will decrease by 1. 

# To deal with boundary issues, a common solution is to allow points leaving the top of an area to come in at the bottom and leaving 
# left, come in on the right (making the space into a Torus). The following code uses the modulus operator (%) which gives and 
# plots the remainder of a division, to ensure agents don't go missing.


    def move(self):
            if random.random() < 0.5:
                self._x = (self._x + 1) % 100
            else:
                self._x = (self._x - 1) % 100
    
            if random.random() < 0.5:
                self._y = (self._y + 1) % 100
            else:
                self._y = (self._y - 1) % 100
                

# The following code makes an eat() method within the Agent class. This code will allow the environment data to be altered. 
# If self.x and self.y are greater than 10 then the environment will lose 10, which will be added to the store. This allows the agents to 
# edit the environment.
    
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

# The following code makes a share_with_neighbours() method within the Agent class. This code will allow the agent to call upon the 
# method to check their neighbourhood; essentially, this will allow the agent to search for close neighbours and share resources with them. 
# The method should work out the distance to each of the other agents and if they fall within the neighbourhood distance it should set 
# it and it's neighbours stores equal to the average of those 2 stores. 

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average
                # the following code prints the code above to test that it is working
                #print("sharing " + str(dist) + " " + str(average))
                
                
                
# The following code calculates the euclidean/straight-line distance to each of the agents using pythagoras theorem
    
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
       
# The following three blocks of code implements a property attribute for each of the coordinates, using appropriate set and get methods.          

# The following code sets the propery x and y.                  
    #@property        
    #def x(self):
        #return self._x
    #def y(self):
        #return self._y
        
# The following code uses the get function to obtain an attribute value for x and y. 

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    
# The following code uses the set function to set the attribute values for x and y.

    def setx(self, value):
        self._x = value 
    def sety(self, value):
        self._y = value
