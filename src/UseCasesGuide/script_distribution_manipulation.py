from openturns import *
from openturns.viewer import ViewImage
from math import *

n = 10
R = 6.0

# Graph Tulipe1
coll = DistributionCollection(n + 1)
for i in range(n):
  theta = 2.0 * pi * i / float(n)
  mean = NumericalPoint(2)
  mean[0] = R * cos(theta)
  mean[1] = R * sin(theta)
  dist = Normal(2)
  dist.setMean(mean)
  coll[i] = Distribution(dist)

coll[n] = Distribution(Normal(NumericalPoint(2, 0.0), NumericalPoint(2, 1.2), CorrelationMatrix(2)))

distribution = Mixture(coll)

xMin = NumericalPoint(2)
xMin[0] = -10.0
xMin[1] = -10.0
xMax = NumericalPoint(2)
xMax[0] = 10.0
xMax[1] = 10.0
pointNumber = NumericalPoint(2)
pointNumber[0] = 101
pointNumber[1] = 101
graph1=distribution.drawPDF(xMin, xMax, pointNumber)
graph1.setTitle("Iso-PDF - Example1")
graph1.draw("contour2D_tulipe", 800, 600, GraphImplementation.PNG)
ViewImage(graph1.getBitmap())

# Graph Tulipe2
coll = DistributionCollection(2)

collMarginal = DistributionCollection(3)
collMarginal[0] = Distribution(Normal(-5,1))
collMarginal[1] = Distribution(Normal(0,2))
collMarginal[2] = Distribution(Normal(6,1))
dist = Mixture(collMarginal)
dist.setName("Marginal 1 :  mixture of normals")

coll[0] = Distribution(dist)

collMarginal[0] = Distribution(Normal(-5,1))
collMarginal[1] = Distribution(Normal(0,1.2))
collMarginal[2] = Distribution(Normal(5,1.5))
dist = Mixture(collMarginal)
dist.setName("Marginal 2 :  mixture of normals")

coll[1] = Distribution(dist)

copula = GumbelCopula(3.5)
#copula = IndependentCopula(2)
distribution = ComposedDistribution(coll, Copula(copula))

xMin[0] = -10.0
xMin[1] = -10.0
xMax[0] = 10.0
xMax[1] = 10.0
pointNumber[0] = 201
pointNumber[1] = 201
graph2=distribution.drawPDF(xMin, xMax, pointNumber)
graph2.setTitle("Iso-PDF - Example2")
graph2.draw("contour2D_2", 800, 600, GraphImplementation.PNG)
ViewImage(graph2.getBitmap())
