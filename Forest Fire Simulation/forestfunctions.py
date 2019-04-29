import pylab as plt
import matplotlib as mpl
import scipy as sp
import random as rd
import copy as cp
import time as tm

def count_states(matrix_):
    # Create a list to store the counts of each type of cell
    counts = [0,0,0,0]
    
    # Create dimensions of the forest
    w,h = sp.shape(matrix_)
    
    # Go through every cell
    for y in range(h):
        for x in range(w):

            # First check the state of the cell
            state = matrix_[x,y]
            
            # Then add to the appropriate state count
            counts[int(state)] = counts[int(state)] + 1
    
    # Print the results
    
    print() # Empty row
    print("empty: " + str(counts[0]))
    print("tree: " + str(counts[1]))
    print("fire: " + str(counts[2]))
    print("charred: " + str(counts[3]))
    print() # Empty row
    
    return list(counts)


# This visualise function will draw the forest each time it is called

def visualise(figure,matrix,time, cm):
    
    # Set the figure that will be worked on
    figure
    
    # Clear whatever was on the plot before
    plt.cla()
    
    # Draw the forest
    plt.pcolor(matrix.T, vmin=0, vmax=3, cmap=cm)

    # Set the scale of x and y as equal
    plt.axis('square')

    # Present the iteration number in the title
    plt.title('time = ' + str(time))
    
    # Save the figure as a .png file
    #plt.savefig(name + '_' + str(time) + '.png')

    # Update the plot on the screen:
    figure.canvas.draw()
    figure.canvas.flush_events()
    
    
def varyforest(i, j, fig1, maxTime, cdict, width=101, height=101, ptree=1.0):
    
    empty, tree, fire, charred = range(4)
    cm = mpl.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)
    time_between_frames = 0.2
    
    # SET INITIAL CONDITIONS
    
    # This line creates an empty grid to represent the forest
    matrix = sp.zeros([width, height])
    
    initial_forest = cp.copy(matrix)

    # CREATING THE TREES
    # Go through the cells from left to right
    for x in range(width):
    
        # And from top to bottom
        for y in range(height):
    
            # Pick a random number
            random = rd.random()
    
            # Plant a tree with probability ptree (number between 0 and 1)
            if random < ptree:
                matrix[x,y] = tree

    # SELECTIVE DEFORESTATION
    constanti = i
    constantj = j

    # Create borders to stop fire from warping from one edge to opposite edge
    matrix[0:101,0] = empty
    matrix[0:101,100] = empty
    matrix[0,0:101] = empty
    matrix[100,0:101] = empty

    # Create horizontal and vertical row thinning by emptying out rows
    while i<width:
        matrix[0:101,i] = empty
        i+=constanti
    
    while j<height:
        matrix[j,0:101] = empty
        j+=constantj
        
    # THE SIMULATION
    
    newmatrix = cp.copy(matrix)
    
    # Show the initial state of the forest
    visualise(fig1,matrix,'initial',cm)

    # Start the fire at a random location
    matrix[rd.randint(0,width-1), rd.randint(0,height-1)] = fire
    
    # Wait for the specified time delay
    initial_delay=2
    tm.sleep(initial_delay)
    
    # Start the timer
    for time in range(maxTime):
    
        # Draw the picture
        visualise(fig1,matrix,time,cm)
        
        # Look at each cell in turn starting at the bottom
        for y in range(height):
            
            # And going from left to right
            for x in range(width):
    
                # First check the state of the cell
                state = matrix[x,y]
    
                # There are two ways that the state can change
    
                # 1) If the cell is on fire, change the state to charred
                if state == fire:
                    state = charred
    
                # 2) If the cell contains a tree, check the neighbouring cells
                # to see whether any of them are on fire
                if state == tree:
                    
                    # Look left and right
                    for dx in [-1,0,1]:
                        
                        # Up and down
                        for dy in [-1,0,1]:
                            
                            # Are any of the neighbours on fire?
                            if matrix[(x+dx)%width, (y+dy)%height] == fire:
                                
                                # If so, tree catches fire
                                state = fire
                
                # Update new state 
                newmatrix[x,y] = state
            
        # Switch the new matrix (which was just recalculated) with the previous one
        # This way, 'matrix' will contain the current state of the forest
        # and 'newmatrix' is ready to be overwritten with the next state again.
        matrix, newmatrix = newmatrix, matrix
        
        # Finally, apply the time delay
        tm.sleep(time_between_frames)
    
    # Draw the final frame
    visualise(fig1,matrix,maxTime,cm)

    current_counts = count_states(matrix)
    with open("data4.txt", "a") as output:
        saveArray = str(current_counts)
        output.write(str(constanti))
        output.write(",")
        output.write(str(constantj))
        output.write(",")
        output.write(saveArray[1:-1])
        output.write("\n")
        
    return 1
    

