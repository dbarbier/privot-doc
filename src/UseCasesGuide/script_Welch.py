#! /usr/bin/python
# -*- coding: iso-8859-15 -*-


from openturns import *

# In the context of the spectral estimate or Fourier transform use,
# we use data blocs with size of form 2^p
size = pow(2, 12)

# We create the time grid
timeGrid = RegularGrid(0., 0.1, size)

# We fix the parameter of the Cauchy model
amplitude = NumericalPoint([5])
scale = NumericalPoint([3])
model = ExponentialCauchy(amplitude, scale)

# Finally, the stochastic process is totally defined
process = SpectralNormalProcess(model, timeGrid)

# We get a sample of 1000 realizations
sample = process.getSample(1000)

# We want now to estimate the density spectrum
# We use the Welch method through the WelchFactory 
filtering = Hanning()
factory = WelchFactory(filtering)

# We get a UserDefinedSpectralModel
ud = factory.build(sample)

# The frequency grid has information such as minFreq, df, maxFreq
freqGrid = ud.getFrequencyGrid()

# With the model, we want to compare values
# We compare values computed with theoritical values 
plotSample = NumericalSample(freqGrid.getN(), 3)

# Loop of comparison ==> data are saved in plotSample 
for k in range(freqGrid.getN()):
  freq = freqGrid.getStart() + k * freqGrid.getStep()  
  plotSample[k,0] = freq
  plotSample[k,1] = abs(ud.computeSpectralDensity(freq)[0, 0])
  plotSample[k,2] = abs(model.computeSpectralDensity(freq)[0, 0])


# Graph section
# We build 2 curves
# each one is function of frequency values
ind = Indices(2)
ind.fill()

graph = Graph()

# The first curve is the estimate density as function of frequency
curve1 = Curve(plotSample.getMarginal(ind))
curve1.setColor('blue')
curve1.setLegendName('estimate model')

# The second curve is the theoritical density as function of frequency
ind[1] = 2
curve2 = Curve(plotSample.getMarginal(ind))
curve2.setColor('red')
curve2.setLegendName('Cauchy model')

graph.add(curve1)
graph.add(curve2)

# some cosmetics : labels, legend position, ...
graph.setXTitle("Frequency")
graph.setYTitle("Spectral density function")
graph.setTitle("Estimate spectral function - Validation")
graph.setLegendPosition('topright')

# finally we draw 
#Show(graph)
graph.draw('welchValidation', 800, 600,  GraphImplementation.PNG)

