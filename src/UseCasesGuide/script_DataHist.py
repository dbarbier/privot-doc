#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage


normal = Normal(0.0,1.0)
sample = normal.getNumericalSample(1000)
data_hist = VisualTest.DrawHistogram(sample)
data_hist.draw("hist_Data", 640,480)
ViewImage(data_hist.getBitmap())
