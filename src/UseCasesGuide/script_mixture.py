#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

triang = Triangular(1.0, 2.0, 4.0)
norm = Normal(-1.0, 1.0)
unif = Uniform(5.0,6.0)
aCollection = DistributionCollection(3)
aCollection[0] = Distribution(triang)
aCollection[1] = Distribution(norm)
aCollection[2] = Distribution(unif)
aCollection[0].setWeight(0.20)
aCollection[1].setWeight(0.50)
aCollection[2].setWeight(0.30)
myMixture = Mixture(aCollection)

myMixture_pdf = myMixture.drawPDF(-3.0,7.0,150)
myMixture_pdf.setLegendPosition("topleft")
myMixture_pdf.draw("pdf_Mixture")
ViewImage(myMixture_pdf.getBitmap())

myMixture_cdf = myMixture.drawCDF(-3.0,7.0,150)
myMixture_cdf.draw("cdf_Mixture")
ViewImage(myMixture_cdf.getBitmap())


