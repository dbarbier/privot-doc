#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

triang = Triangular(1.0, 2.0, 4.0)
norm = Normal(-1.0, 1.0)
unif = Uniform(2.0, 3.0)
aCollection = DistributionCollection(3)
aCollection[0] = Distribution(triang)
aCollection[1] = Distribution(norm)
aCollection[2] = Distribution(unif)
aCollection[0].setWeight(0.20)
aCollection[1].setWeight(0.50)
aCollection[2].setWeight(0.30)
myDistribution = Mixture(aCollection)


# Mixture
myDistribution_pdf = myDistribution.drawPDF(-4.0,8.0,150)
myDistribution_pdf.draw("pdf_Mixture", 640,480)
ViewImage(myDistribution_pdf.getBitmap())

myDistribution_cdf = myDistribution.drawCDF(-4.0,8.0,150)
myDistribution_cdf.draw("cdf_Mixture", 640,480)
ViewImage(myDistribution_cdf.getBitmap())



