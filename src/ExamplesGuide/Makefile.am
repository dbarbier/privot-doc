#                                               -*- Makefile -*-
#
#  Makefile.am
#
#  (C) Copyright 2005-2012 EDF-EADS-Phimeca
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License.
#
#  This library is distributed in the hope that it will be useful
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
#  @author: $LastChangedBy$
#  @date:   $LastChangedDate$
#  Id:      $Id$
#
include $(top_srcdir)/config/common.am

COMMON_SOURCES = \
	$(top_builddir)/src/GenericInformation.tex \
	$(top_srcdir)/src/logoOpenTURNS.jpg \
	OpenTURNS_ExamplesGuide.tex \
	resultatExampleBeam.tex \
	scriptExample_beam.py \
	Treillis.pdf \
	Truss_errors.pdf \
	Truss_SA.pdf \
	Truss_histo.png 

PDF_SOURCES = \
	Math_Notations.sty \
	convergenceGrapheDS.pdf \
	convergenceGrapheIS.pdf \
	convergenceGrapheLHS.pdf \
	convergenceGrapheMonteCarlo.pdf \
	distributionE_pdf.pdf \
	distributionF_pdf.pdf \
	distributionI_pdf.pdf \
	distributionL_pdf.pdf \
	ImportanceFactorsDrawingFORM.pdf \
	PCE_LaguerrePolynomials_VariableF.pdf \
	PCE_JacobiPolynomials_VariableI.pdf \
	PCE_JacobiPolynomials_VariableE.pdf \
	PCE_LegendrePolynomials_VariableL.pdf \
	PCE_comparisonModels.pdf \
	poutre.pdf \
	smoothedCDF.pdf \
	smoothedPDF.pdf \
	smoothedPDF_and_GaussianPDF.pdf

XML_SOURCES = \
	Math_Notations.plt \
	convergenceGrapheDS.png \
	convergenceGrapheIS.png \
	convergenceGrapheLHS.png \
	convergenceGrapheMonteCarlo.png \
	distributionE_pdf.png \
	distributionF_pdf.png \
	distributionI_pdf.png \
	distributionL_pdf.png \
	ImportanceFactorsDrawingFORM.png \
	PCE_LaguerrePolynomials_VariableF.png \
	PCE_JacobiPolynomials_VariableI.png \
	PCE_JacobiPolynomials_VariableE.png \
	PCE_LegendrePolynomials_VariableL.png \
	PCE_comparisonModels.png \
	poutre.png \
	smoothedCDF.png \
	smoothedPDF.png \
	smoothedPDF_and_GaussianPDF.png

OpenTURNS_ExamplesGuide.pdf: $(COMMON_SOURCES) $(PDF_SOURCES)

OpenTURNS_ExamplesGuide.xml: $(COMMON_SOURCES) $(XML_SOURCES)

pdf-local: OpenTURNS_ExamplesGuide.pdf
doc_DATA  = OpenTURNS_ExamplesGuide.pdf
EXTRA_DIST = $(COMMON_SOURCES) $(PDF_SOURCES)

if WITH_TRALICS
if WITH_LIBXSLT
html-local: OpenTURNS_ExamplesGuide.tgz
install-html-local: OpenTURNS_ExamplesGuide.installed
EXTRA_DIST += $(XML_SOURCES)
endif
endif