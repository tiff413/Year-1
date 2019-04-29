import pylab as plt
import matplotlib as mpl
import scipy as sp
import random as rd
import copy as cp
import time as tm
import forestfunctions as ff

#-----------------------------------------------------------------------
# VISUALISATION

# This section sorts out the colours in the animation
# First, by telling python what colours to use (as rgb values)
cdict = {
      'red'  :  ( (0.0, 1.0, 1.0),
                  (0.3, 0.0, 0.0),
                  (0.6, 255./256, 255./256),
                  (1.0, 0.0, 0.0)),

      'green':  ( (0.0, 1.0, 1.0),
                  (0.3, 1.0, 1.0),
                  (0.6, 160./256, 160./256),
                  (1.0, 0.0, 0.0)),
                  
      'blue' :  ( (0.0, 1.0, 1.0),
                  (0.3, 0.0, 0.0),
                  (0.6, 0.0, 0.0),
                  (1.0, 0.0, 0.0))
            }

cm = mpl.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)

# Then by assigning a colour value to each state
empty, tree, fire, charred = range(4)

# Turn on interactive plotting (to animate the simulation)
plt.ion()

# Create the figure on which to plot
fig1 = plt.figure(num=1)

# Show the figure (empty at the moment)
# The .canvas.draw() and .canvas.flush_events() allow for live updating
fig1.clear()
plt.show()
fig1.canvas.draw()
fig1.canvas.flush_events()

#-----------------------------------------------------------------------
# SET SIMULATION PARAMETERS

# Choose length of simulation
maxTime = 43
# Set the size of the region
width = 101
height = 101

# Choose a file name for the initial and final images
name = 'forestpic'

# Choose the density of the forest
# (A number between 0 and 1 which represents 
# the probability that each cell will have a tree)
ptree = 1.0

# The next two parameters control the speed of the simulation.

# Choose an initial delay (in seconds) before the simulation starts:
initial_delay = 2

# Set a minimum time interval (in seconds) between frames:
# (The simulation will slow down for larger forests anyway)
time_between_frames = 0.2

#------------------------------------------------------------------------
# EXECUTE THE SIMULATION OVER A LOOP

# Iterate the simulation to incrementally test grids of varying
# lengths and widths
for j in range(2,51):   
    for i in range(2,51):
        ff.varyforest(i, j, fig1, maxTime, cdict)
    ff.varyforest(i, j, fig1, maxTime, cdict)
    

