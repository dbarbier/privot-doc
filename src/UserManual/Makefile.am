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
#  @author: $LastChangedBy: schueller $
#  @date:   $LastChangedDate: 2012-02-27 14:48:06 +0100 (lun. 27 févr. 2012) $
#  Id:      $Id: Makefile.am 1539 2012-02-27 13:48:06Z schueller $
#
include $(top_srcdir)/config/common.am

COMMON_SOURCES = \
	$(top_builddir)/src/GenericInformation.tex \
	$(top_srcdir)/src/logoOpenTURNS.jpg \
	OpenTURNS_UserManual_TUI.sty \
	BaseObjects_UserManual.tex \
	ExperimentPlane_UserManual.tex \
	FFT_UserManual.tex \
	Function_UserManual.tex \
	Graphs_UserManual.tex \
	NonParametricResponseSurfaceApproximation_FCE_UserManual.tex \
	OpenTURNS_UserManual_TUI.tex \
	Optimization_UserManual.tex \
	ParametricResponseSurfaceApproximation_UserManual.tex \
	Polynomials_UserManual.tex \
	ProbabilisticModeling_UserManual.tex \
	QuadraticCumul_UserManual.tex \
	Statistics_UserManual.tex \
	Stochastic_Process_UserManual.tex \
	ThresholdProbabilityReliabilityAlgorithm_UserManual.tex \
	ThresholdProbabilitySimulationAlgorithm_UserManual.tex \
	user_manual_title.tex

PDF_SOURCES = \
	Math_Notations.sty

XML_SOURCES = \
        Math_Notations.plt

OpenTURNS_UserManual_TUI.pdf: $(COMMON_SOURCES) $(PDF_SOURCES)

OpenTURNS_UserManual_TUI.xml: $(COMMON_SOURCES) $(XML_SOURCES)

pdf-local: OpenTURNS_UserManual_TUI.pdf

doc_DATA  = OpenTURNS_UserManual_TUI.pdf
EXTRA_DIST = $(COMMON_SOURCES) $(PDF_SOURCES)

if WITH_TRALICS
if WITH_LIBXSLT
html-local: OpenTURNS_UserManual_TUI.tgz
install-html-local: OpenTURNS_UserManual_TUI.installed
EXTRA_DIST += $(XML_SOURCES)
endif
endif

