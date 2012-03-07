#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import ViewImage


sample1 = Normal(NumericalPoint(2,0.0),NumericalPoint(2,1.0), IdentityMatrix(2)).getNumericalSample(1000)
sample2 = Normal(NumericalPoint(2,1.0),NumericalPoint(2,1.0), IdentityMatrix(2)).getNumericalSample(1000)
myGraph = Graph("Distribution 1 sample", "x1", "x2", True, "topright")

myCloud1 = Cloud(sample1, "blue", "fsquare","First Cloud")
myGraph.add(Drawable(myCloud1))

myCloud2 = Cloud(sample2, "red", "circle","Second Cloud")
myGraph.add(Drawable(myCloud2))
myGraph.draw("cloud2", 640, 480)
ViewImage(myGraph.getBitmap())
