#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

myFunction = NumericalMathFunction("poutre")

distributionE = Beta(0.94,3.19,2.78e7,4.83e7)
distributionF = LogNormal(30000.0, 9000.0, 15000, 1)
distributionL = Uniform(250, 260)
distributionI = Beta(2.5,4.0,3.1e2,4.5e2)

collectionMarginales = DistributionCollection(4)
collectionMarginales[0] = Distribution(distributionE)
collectionMarginales[1] = Distribution(distributionF)
collectionMarginales[2] = Distribution(distributionL)
collectionMarginales[3] = Distribution(distributionI)


inputDistribution = ComposedDistribution(collectionMarginales, Copula(IndependentCopula(4)))

inputDesc = Description(4)
inputDesc[0] = "E"
inputDesc[1] = "F"
inputDesc[2] = "L"
inputDesc[3] = "I"
inputDistribution.setDescription(inputDesc)


input = RandomVector(inputDistribution)
descrip = Description(4)
descrip[0]  ="E"
descrip[1]  ="F"
descrip[2]  ="L"
descrip[3]  ="I"
input.setDescription(descrip)

output =  RandomVector(myFunction, input)




myCobyla = Cobyla()
myCobyla.setSpecificParameters(CobylaSpecificParameters())
myCobyla.setMaximumIterationsNumber(500)
myCobyla.setMaximumAbsoluteError(1.0e-10)
myCobyla.setMaximumRelativeError(1.0e-10)
myCobyla.setMaximumResidualError(1.0e-10)
myCobyla.setMaximumConstraintError(1.0e-10)

myEvent = Event(output, ComparisonOperator(Less()), -30, "Event 1")

mean = input.getMean()
myAlgo = FORM(NearestPointAlgorithm(myCobyla), myEvent, mean)
myAlgo.run()
result = myAlgo.getResult()


####################################
# Graph 1 : Importance Factors graph
importanceFactorsGraph = result.drawImportanceFactors()
importanceFactorsGraph.draw("ImportanceFactorsDrawingFORM")

# View the bitmap file
ViewImage(importanceFactorsGraph.getBitmap())


####################################
# Graph 2 : Hasofer Reliability Index Sensitivity Graphs graph
reliabilityIndexSensitivityGraphs = result.drawHasoferReliabilityIndexSensitivity()

# Sensitivity to parameters of the marginals of
# the input probabilistic vector
graph2a = reliabilityIndexSensitivityGraphs[0]
graph2a.setLegendPosition("bottomright")
graph2a.draw("HasoferReliabilityIndexMarginalSensitivityDrawing", 640, 480)

# View the bitmap file
ViewImage(graph2a.getBitmap())

####################################
# Graph 3 : FORM Event Probability Sensitivity Graphs graph
eventProbabilitySensitivityGraphs = result.drawEventProbabilitySensitivity()

# Sensitivity to parameters of the marginals of the input probabilistic vector
graph3a = eventProbabilitySensitivityGraphs[0]
graph3a.draw("EventProbabilityIndexMarginalSensitivityDrawing")

# View the bitmap file
ViewImage(graph3a.getBitmap())


####################################
