from openturns import *


# Create the function
inputVar = Description(['X1', 'X2'])
formula = Description(['X1*X1+X2'])
outputVar = Description(['Y'])
myFCT = NumericalMathFunction(inputVar, outputVar, formula)

# Generate some inputValues
N = 500
cor = CorrelationMatrix(2)
cor[0,1] = -0.6
inputSample = Normal(NumericalPoint(2),cor).getNumericalSample(N)
inputSample.setDescription(inputVar)

outputSample = myFCT(inputSample)
outputSample.setDescription(outputVar)

# CobWeb

# Graph 1 : value based
#minValue = 3
#maxValue = 20
#myCobweb = VisualTest.DrawCobWeb(inputSample, outputSample, minValue, maxValue, 'red', False)
#Show(myCobweb)

# Graph 2 : rank based
minValue = 0.9
maxValue = 1
myCobweb = VisualTest.DrawCobWeb(inputSample, outputSample, minValue, maxValue, 'red', True)
bb = myCobweb.getBoundingBox()
bb[1] = 1.1*bb[1]
myCobweb.setBoundingBox(bb)
Show(myCobweb)

myCobweb.draw('cobWeb', 640, 480, GraphImplementation.PNG)
