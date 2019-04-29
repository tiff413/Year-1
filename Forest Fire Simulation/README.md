Is selective deforestation an effective method for combatting forest fires and how can this strategy be used most effectively?

Every year, in the US alone, more than 100,000 wildfires destroy 4 to 5 million acres of land (National Geographic, n.d.). As the issue worsens, researchers have developed methods to mitigate the impacts of wildfires, one being selective deforestation.

These programs focus on the row thinning technique where trees are removed to form plots of forest with a fixed distance between each deforested row and column, creating grid-like plots of forest. The ideal pattern would minimise damage from forest fires and minimise trees required to be deforested. 

The distance between each empty row (height of divided plots) is given by i, and for columns (width of divided plots) it is given by j. The aim was to loop the entire simulation after each increment of j or increment of i within j to simulate forest fires on different grid/plot dimensions. The results were be stored in an external .txt file. 

forestfunctions.py contains functions that will:
  1. Simulate a randomly situated forest fire on a rectangular area of forest
  2. Show how many trees are deforested (empty), healthy (tree), on fire (fire), burnt (charred)
  3. Selectivelty and evenly deforest i rows and j columns of trees to form a grid pattern

forestfunctions.py contains all the functions required for the simulation. Whereas forest.py is where the user can play around with parameters and change the way the simulation is executed.

Parameters that can be changed in forest.py include:
  1. Total time of simulation
  2. Size of region
  3. Probability of density of forest
  4. Speed of simulation
  5. Iterate over i and j to change the length and width of the grid pattern
  

