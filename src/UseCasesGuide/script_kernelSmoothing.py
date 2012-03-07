#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

triang = Triangular(1.0, 2.0, 4.0)
norm = Normal(-1.0, 1.0)
norm2 = Normal(3.0, 1.0)
aCollection = DistributionCollection(3)
aCollection[0] = Distribution(triang)
aCollection[1] = Distribution(norm)
aCollection[2] = Distribution(norm2)
aCollection[0].setWeight(0.20)
aCollection[1].setWeight(0.50)
aCollection[2].setWeight(0.30)
myDistribution = Mixture(aCollection)


# Mixture
myDistribution_pdf = myDistribution.drawPDF(-4.0,8.0,150)
myDistribution_pdf_draw = myDistribution_pdf.getDrawable(0)
myDistribution_pdf_draw.setColor("black")
myDistribution_pdf_draw.setLegendName("Real distribution")
myDistribution_pdf.setDrawable(myDistribution_pdf_draw,0)

myDistribution_pdf2 = Graph(myDistribution_pdf)

myDistribution_cdf = myDistribution.drawCDF(-4.0,8.0,150)
myDistribution_cdf_draw = myDistribution_cdf.getDrawable(0)
myDistribution_cdf_draw.setColor("black")
myDistribution_cdf_draw.setLegendName("Real distribution")
myDistribution_cdf.setDrawable(myDistribution_cdf_draw,0)

myDistribution_cdf2 = Graph(myDistribution_cdf)

# Sample
sample = myDistribution.getNumericalSample(10000)


#####################################
# Bandwith selection :   automatic method
# n=10^4 so it is the mixted method
#####################################


# Normal kernel smoothing

kernel = KernelSmoothing()
gaussianSmoothed = kernel.build(sample)

gaussianSmoothedPDF = gaussianSmoothed.drawPDF(-4,8,251)
gaussianSmoothedPDF_draw = gaussianSmoothedPDF.getDrawables()[0]
gaussianSmoothedPDF_draw.setColor("blue")
gaussianSmoothedPDF_draw.setLegendName("normal kernel")
myDistribution_pdf.add(gaussianSmoothedPDF_draw)
##myDistribution_pdf.setTitle("Gaussian Kernel Smoothing PDF")
##myDistribution_pdf.draw("pdf_gaussKernelSmooth", 640,480)
##ViewImage(myDistribution_pdf.getBitmap())

gaussianSmoothedCDF = gaussianSmoothed.drawCDF(-4,8,251)
gaussianSmoothedCDF_draw = gaussianSmoothedCDF.getDrawables()[0]
gaussianSmoothedCDF_draw.setColor("blue")
gaussianSmoothedCDF_draw.setLegendName("normal kernel")
myDistribution_cdf.add(gaussianSmoothedCDF_draw)
##myDistribution_cdf.setTitle("Gaussian Kernel Smoothing CDF")
##myDistribution_cdf.draw("cdf_gaussKernelSmooth", 640,480)
##ViewImage(myDistribution_cdf.getBitmap())

# Triangular kernel smoothing

kernel = KernelSmoothing(Distribution(Triangular()))
triangularSmoothed = kernel.build(sample)

triangularSmoothedPDF = triangularSmoothed.drawPDF(-4,8,251)
triangularSmoothedPDF_draw = triangularSmoothedPDF.getDrawables()[0]
triangularSmoothedPDF_draw.setColor("green")
triangularSmoothedPDF_draw.setLegendName("triangular kernel")
myDistribution_pdf.add(triangularSmoothedPDF_draw)

triangularSmoothedCDF = triangularSmoothed.drawCDF(-4,8,251)
triangularSmoothedCDF_draw = triangularSmoothedCDF.getDrawables()[0]
triangularSmoothedCDF_draw.setColor("green")
triangularSmoothedCDF_draw.setLegendName("triangular kernel")
myDistribution_cdf.add(triangularSmoothedCDF_draw)


# Epanechnikov kernel smoothing

kernel = KernelSmoothing(Distribution(Epanechnikov()))
epanechnikovSmoothed = kernel.build(sample)

epanechnikovSmoothedPDF = epanechnikovSmoothed.drawPDF(-4,8,251)
epanechnikovSmoothedPDF_draw = epanechnikovSmoothedPDF.getDrawables()[0]
epanechnikovSmoothedPDF_draw.setColor("red")
epanechnikovSmoothedPDF_draw.setLegendName("epanechnikov kernel")
myDistribution_pdf.add(epanechnikovSmoothedPDF_draw)

epanechnikovSmoothedCDF = epanechnikovSmoothed.drawCDF(-4,8,251)
epanechnikovSmoothedCDF_draw = epanechnikovSmoothedCDF.getDrawables()[0]
epanechnikovSmoothedCDF_draw.setColor("red")
epanechnikovSmoothedCDF_draw.setLegendName("epanechnikov kernel")
myDistribution_cdf.add(epanechnikovSmoothedCDF_draw)

# Show the graph

myDistribution_pdf.setTitle("Effect of the kernel selection")
myDistribution_pdf.draw("kernelSmoothing_pdf")
ViewImage(myDistribution_pdf.getBitmap())

myDistribution_cdf.setTitle("Effect of the kernel selection")
myDistribution_cdf.setLegendPosition("bottomright")
myDistribution_cdf.draw("kernelSmoothing_cdf")
ViewImage(myDistribution_cdf.getBitmap())




# Boundary treatment

exp = Exponential(2.0, 0.0)

expPDF = exp.drawPDF()
expPDF_draw = expPDF.getDrawable(0)
expPDF_draw.setColor("black")
expPDF.setDrawable(expPDF_draw,0)

expCDF = exp.drawCDF()
expCDF_draw = expCDF.getDrawable(0)
expCDF_draw.setColor("black")
expCDF.setDrawable(expCDF_draw,0)

sample2 = exp.getNumericalSample(10000)
kernel = KernelSmoothing()

# whith boundary treatment
smoothedBoundary = kernel.build(sample2, True)
smoothedBoundaryPDF = smoothedBoundary.drawPDF()
smoothedBoundaryPDF_draw = smoothedBoundaryPDF.getDrawable(0)
smoothedBoundaryPDF_draw.setLegendName("whith boundary treatment")
expPDF.add(smoothedBoundaryPDF_draw)

smoothedBoundaryCDF = smoothedBoundary.drawCDF()
smoothedBoundaryCDF_draw = smoothedBoundaryCDF.getDrawable(0)
smoothedBoundaryCDF_draw.setLegendName("whith boundary treatment")
expCDF.add(smoothedBoundaryCDF_draw)

# whithout boundary treatment
smoothedNoBoundary = kernel.build(sample2)
smoothedNoBoundaryPDF = smoothedNoBoundary.drawPDF()
smoothedNoBoundaryPDF_draw = smoothedNoBoundaryPDF.getDrawable(0)
smoothedNoBoundaryPDF_draw.setColor("blue")
smoothedNoBoundaryPDF_draw.setLegendName("whithout boundary treatment")
expPDF.add(smoothedNoBoundaryPDF_draw)

smoothedNoBoundaryCDF = smoothedNoBoundary.drawCDF()
smoothedNoBoundaryCDF_draw = smoothedNoBoundaryCDF.getDrawable(0)
smoothedNoBoundaryCDF_draw.setColor("blue")
smoothedNoBoundaryCDF_draw.setLegendName("whithout boundary treatment")
expCDF.add(smoothedNoBoundaryCDF_draw)


# Show the graph
expPDF.setTitle("Effect of the boundary treatment")
expPDF.draw("kernelSmoothing_boundary_pdf")
ViewImage(expPDF.getBitmap())

expCDF.setTitle("Effect of the boundary treatment")
expCDF.setLegendPosition("bottomright")
expCDF.draw("kernelSmoothing_boundary_cdf")
ViewImage(expCDF.getBitmap())

