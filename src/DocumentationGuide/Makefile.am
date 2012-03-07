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
	OpenTURNS_DocumentationGuide.tex

OpenTURNS_DocumentationGuide.pdf: $(COMMON_SOURCES)

OpenTURNS_DocumentationGuide.xml: $(COMMON_SOURCES)

pdf-local: OpenTURNS_DocumentationGuide.pdf
if WITH_TRALICS
if WITH_LIBXSLT
html-local: OpenTURNS_DocumentationGuide.tgz
install-html-local: OpenTURNS_DocumentationGuide.installed
endif
endif

doc_DATA  = OpenTURNS_DocumentationGuide.pdf
EXTRA_DIST = $(COMMON_SOURCES)
