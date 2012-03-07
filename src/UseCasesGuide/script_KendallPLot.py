from openturns import *



# KendallPlot tests

# Case 1 : Test of a copula to a sample

# Create the sample
size = 100
copula = FrankCopula(1.5)
copula2 = GumbelCopula(4.5)

sample1 = copula.getNumericalSample(size)
sample1.setName("data 1")

# The test says ok
kendallPlot1 = VisualTest.DrawKendallPlot(sample1, copula)
kendallPlot1.setTitle('Kendall Plot : data vs Frank copula')
Show(kendallPlot1)
kendallPlot1.draw("KendallPlotCopula", 640, 480, GraphImplementation.PNG)
kendallPlot1.draw("KendallPlotCopula", 640, 480, GraphImplementation.PDF)


# The test says no
kendallPlot2 = VisualTest.DrawKendallPlot(sample1, copula2)
kendallPlot2.setTitle('Kendall Plot : data vs Gumbel copula')
Show(kendallPlot2)
kendallPlot2.draw("KendallPlotCopulaBad", 640, 480, GraphImplementation.PNG)
kendallPlot2.draw("KendallPlotCopulaBad", 640, 480, GraphImplementation.PDF)



# Case 2 : Test whether two samples have the same copula

sample2 = copula.getNumericalSample(size)
sample2.setName("data 2")
sample3 = copula2.getNumericalSample(size)
sample3.setName("data 3")


# The test says ok
kendallPlot3 = VisualTest.DrawKendallPlot(sample2, sample1)
kendallPlot3.setTitle('Kendall Plot : data 1 vs data 2')
Show(kendallPlot3)
kendallPlot3.draw("KendallPlotSample", 640, 480, GraphImplementation.PNG)
kendallPlot3.draw("KendallPlotSample", 640, 480, GraphImplementation.PDF)

# The test says no
kendallPlot4 = VisualTest.DrawKendallPlot(sample3, sample1)
kendallPlot4.setTitle('Kendall Plot : data 1 vs data 3')
Show(kendallPlot4)
kendallPlot4.draw("KendallPlotSampleBad", 640, 480, GraphImplementation.PNG)
kendallPlot4.draw("KendallPlotSampleBad", 640, 480, GraphImplementation.PDF)
