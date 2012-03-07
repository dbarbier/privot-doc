#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage

normal = Normal(0.0, 1.0)
sample = normal.getNumericalSample(1000)

sampleHenryLine = VisualTest.DrawHenryLine(sample)
sampleHenryLine.draw("HenryLineTestRight", 640,480)
ViewImage(sampleHenryLine.getBitmap())

sample2 = Beta(0.7, 1.6, 0.0, 2.0).getNumericalSample(1000)
sample2HenryLine = VisualTest.DrawHenryLine(sample2)
sample2HenryLine.draw("HenryLineTestFalse", 640,480)
ViewImage(sample2HenryLine.getBitmap())
