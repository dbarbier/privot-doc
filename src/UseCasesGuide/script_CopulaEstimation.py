
from openturns import *

# Creation of a bidimensional distribution


# Creation of the 2d distributino
myDist = ComposedDistribution(DistributionCollection([Normal(), Normal()]), Copula(ClaytonCopula(2.5)))

# Creation of a sample
initSample = myDist.getNumericalSample(500)

# Draw a cloud
initCloud = Cloud(initSample, 'blue', 'plus', 'initial sample')
graphInit =  Graph('Inital sample', 'X', 'Y', True, 'topleft')
graphInit.add(initCloud)
Show(graphInit)
graphInit.draw('initSample', 640,480,GraphImplementation.PNG)

# Creation of the operator which transforms the marginals into the uniform ones
ranksTransf = MarginalTransformationEvaluation(DistributionCollection([Normal(), Normal()]), MarginalTransformationEvaluation.FROM)


# Transformation of the initial sample into the ranked sample
transformedSample = NumericalSample(initSample.getSize(), initSample.getDimension())
for i in range(initSample.getSize()) :
  transformedSample[i] = ranksTransf(initSample[i])
#print transformedSample

# Cloud of the ranked points
rankedCloud = Cloud(transformedSample, 'blue', 'plus', 'ranks sample')
graphRanks =  Graph('Ranks sample', 'X', 'Y', True, 'topleft')
graphRanks.add(rankedCloud)
Show(graphRanks)
graphRanks.draw('ranksSample', 640,480,GraphImplementation.PNG)

myGraph = Graph('Parametric estimation of the copula', 'X', 'Y', True, 'topleft')
myGraph.add(rankedCloud)

# Estimation of a copula on the ranked points cloud
estimatedCopula = ClaytonCopulaFactory().build(transformedSample)
print estimatedCopula

# Superposition of the iso-curves of the copula estimated on the points cloud
minPoint = NumericalPoint([0.0, 0.0])
maxPoint = NumericalPoint([1.0, 1.0])
pointNumber = NumericalPoint([201, 201])
graphEstimatedCopula = estimatedCopula.drawPDF(minPoint, maxPoint, pointNumber)
contour_estimatedCopula = graphEstimatedCopula.getDrawable(0)
contour_estimatedCopula.setDrawLabels(False)

# Levels of the iso curves
nlev = 31
levels = NumericalPoint(nlev)
for i in range(nlev):
  levels[i] = 0.25 * nlev / (1.0 + i)

contour_estimatedCopula.setLevels(levels)
contour_estimatedCopula.setLegendName('Clayton copula iso-PDF')
graphEstimatedCopula.setDrawable(contour_estimatedCopula, 0)

graphEstimatedCopula_draw = graphEstimatedCopula.getDrawable(0)
graphEstimatedCopula_draw.setColor('red')
myGraph.add(graphEstimatedCopula_draw)
myGraph.setLegendPosition('bottomright')
Show(myGraph)

myGraph.draw('copula_estimation', 640, 480, GraphImplementation.PNG)
