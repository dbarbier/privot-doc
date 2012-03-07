#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

collection = HistogramPairCollection(3)
collection[0] = HistogramPair(1., 1.)
collection[1] = HistogramPair(4., 2.)
collection[2] = HistogramPair(2., 3.)
histogram = Histogram(0., collection)
histogram_pdf = histogram.drawPDF()
histogram_pdf.draw("pdf_Histogram", 640,480)
ViewImage(histogram_pdf.getBitmap())

histogram_cdf = histogram.drawCDF()
histogram_cdf.draw("cdf_Histogram", 640,480)
ViewImage(histogram_cdf.getBitmap())
