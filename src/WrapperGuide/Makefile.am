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
	Appendix1.tex \
	Appendix2.tex \
	Appendix3.tex \
	Appendix4.tex \
	ExternalCodeInterface.tex \
	FunctionTypes.tex \
	FutureDevelopments.tex \
	Introduction.tex \
	OpenTURNS_WrappersGuide.tex \
	Summary.tex \
	WrapperStructure.tex \
	Wrapper.tex

PDF_SOURCES = \
	Figure1.pdf \
	Figure2.pdf \
	Figure3.pdf \
	Figure4.pdf \
	Figure5.pdf \
	Figure6.pdf \
	Figure7.pdf \
	Figure8.pdf

XML_SOURCES = \
	Figure1.png \
	Figure2.png \
	Figure3.png \
	Figure4.png \
	Figure5.png \
	Figure6.png \
	Figure7.png \
	Figure8.png

OpenTURNS_WrappersGuide.pdf: $(COMMON_SOURCES) $(PDF_SOURCES)

OpenTURNS_WrappersGuide.xml: $(COMMON_SOURCES) $(XML_SOURCES)

pdf-local: OpenTURNS_WrappersGuide.pdf

doc_DATA = OpenTURNS_WrappersGuide.pdf
EXTRA_DIST = $(COMMON_SOURCES) $(PDF_SOURCES)

if WITH_TRALICS
if WITH_LIBXSLT
html-am: OpenTURNS_WrappersGuide.tgz
install-html-am: OpenTURNS_WrappersGuide.installed
EXTRA_DIST += $(XML_SOURCES)
endif
endif