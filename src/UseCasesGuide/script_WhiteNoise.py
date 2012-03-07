from openturns import *

# Time grid over which all the processes will be defined
nt = 100

timeGrid = RegularGrid(0.0, 1.0, nt)

# Definition of the distribution
sigma = 1.0
myDistribution = Normal(0., sigma)

# Definition of the process
myProcess = WhiteNoise(myDistribution, timeGrid)

# We get a realization of the white noise process
realization = myProcess.getRealization()


# The realization is a time series
# we draw it as function of time thanks to the drawMarginal method
# We rework the legend name and color to have pretty graph 
graph = Graph()
marginalDraw = realization.drawMarginal(0)
drawable = marginalDraw.getDrawable(0)
drawable.setLegendName('realization')
drawable.setColor('blue')
graph.add(drawable)

graph.setXTitle('Time')
graph.setYTitle('Values')
graph.setTitle("White noise process")
graph.setLegendPosition('topright')
graph.draw("whitenoise_realization", 800, 600, GraphImplementation.PNG)

# Several realization ==> here we fix 5 in order to be able to compare and visualize difference
sample = myProcess.getSample(5)
graphSample = sample.drawMarginal(0)
graphSample.setTitle("5 realizations of the White noise process")
for k in range(5):
  drawable = graphSample.getDrawable(k)
  drawable.setLegendName('realization ' + str(k+1))
  graphSample.setDrawable(drawable, k)

graphSample.draw("whitenoise_realizations", 800, 600, GraphImplementation.PNG)

