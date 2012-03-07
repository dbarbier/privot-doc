#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

beta = Beta(1.2,3.4,1.0, 2.0)
sample = beta.getNumericalSample(1000)

betaPDF = beta.drawPDF()
betaPDF.draw("BetaPDFajeter",  640,480)
ViewImage(betaPDF.getBitmap())

sampleQQplot = VisualTest.DrawQQplot(sample,Distribution(beta),100)
sampleQQplot.draw("beta_QQplot", 640,480)
ViewImage(sampleQQplot.getBitmap())

weibull = Weibull(1.5, 1.0, 1.0)
sampleFalseQQplot = VisualTest.DrawQQplot(sample,Distribution(weibull),100)
sampleFalseQQplot.draw("weibull_QQplot", 640,480)
ViewImage(sampleFalseQQplot.getBitmap())
