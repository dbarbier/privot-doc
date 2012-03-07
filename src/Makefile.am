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

DIRS         = .
DIRS        += ArchitectureGuide
DIRS        += DocumentationGuide
DIRS        += ReferenceGuide
DIRS        += UseCasesGuide
DIRS        += UserManual
DIRS        += ExamplesGuide
DIRS        += WrapperGuide
DIRS        += GNU_free_documentation_licence
DIRS        += ContributionGuide
DIRS        += WindowsPortGuide
DIRS        += CodingRulesGuide

EXTRA_DIST   = \
        OpenTURNS.css \
        logoOpenTURNS.jpg \
        NextButton.png \
        PreviousButton.png \
        UpButton.png

SUBDIRS      =  $(DIRS)
DIST_SUBDIRS =  $(DIRS)

BUILT_SOURCES = GenericInformation.tex
