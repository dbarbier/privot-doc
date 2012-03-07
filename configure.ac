#                                               -*- Autoconf -*-
#
#  configure.ac
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
#  Id:      $Id: configure.ac 1539 2012-02-27 13:48:06Z schueller $
#
#  Process this file with autoconf to produce a configure script.
#  Set minimal version of Autoconf for configure to work
#
AC_PREREQ([2.59])

# Initialize Autoconf
AC_INIT([OpenTURNS platform documentation],
        [February2012],
        [bugs@openturns.org],
        [openturns-doc])

OPENTURNS_VERSION="1.0rc1"
AC_SUBST([OPENTURNS_VERSION])

# We check a special cache variable to see if we are built in a combined environment
AC_CACHE_CHECK([for combined build process], [ot_cv_combined_env], [ot_cv_combined_env=no])

# Choose our own configuration directory
AC_CONFIG_AUX_DIR([config])
AC_SUBST([ac_aux_dir])

# Initialize Automake
AM_INIT_AUTOMAKE([dist-bzip2 tar-ustar])

# Check that source files are available
AC_CONFIG_SRCDIR([src/DocumentationGuide/OpenTURNS_DocumentationGuide.tex])


# Propagate through source files the path of the installation directory
AC_DEFINE_UNQUOTED([INSTALL_PATH], "$prefix", [The path of installation])


# Proceed to required program detection
AC_PROG_AWK
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET


# Proceed to required or optional program detection
# with our own macro files

# Check for Open TURNS library
# OT_CHECK_OPENTURNS


# Write out configure arguments
ot_configure_args=`eval echo configure $ac_configure_args`
AC_SUBST(ot_configure_args)

# Write out configuration date
AC_PATH_PROG([DATE], [date], [:])
ot_configure_date=`$DATE -R`
AC_SUBST(ot_configure_date)

# Write out project revision if versioning tool is present
AC_PATH_PROG([SVNVERSION], [svnversion], [echo unknown])
#_AC_SRCDIRS([.])
ot_revision=`cd "$ac_top_srcdir" && $SVNVERSION`
AC_SUBST(ot_revision)

# Check LaTeX tools
OT_CHECK_PDFLATEX
OT_CHECK_MAKEINDEX
OT_CHECK_BIBTEX
OT_CHECK_TRALICS
OT_CHECK_LIBXSLT
AC_SUBST(ac_top_srcdir)
AC_SUBST(ac_abs_top_srcdir)

# Propagate configuration into Makefile
AC_OUTPUT([src/GenericInformation.tex
	   Makefile
           m4/Makefile
           config/Makefile
           latex2html/Makefile
           src/Makefile
           src/GNU_free_documentation_licence/GNU_Free_Documentation_License_GNU_Project_Free_Software_Foundation_FSF_fichiers/Makefile
           src/GNU_free_documentation_licence/Makefile
           src/UserManual/Makefile
           src/UseCasesGuide/Makefile
           src/DocumentationGuide/Makefile
           src/WrapperGuide/Makefile
           src/ArchitectureGuide/Figures/analysis/Makefile
           src/ArchitectureGuide/Figures/modeling_notions/Makefile
           src/ArchitectureGuide/Figures/design/Makefile
           src/ArchitectureGuide/Figures/Makefile
           src/ArchitectureGuide/Makefile
           src/ReferenceGuide/Makefile
           src/ContributionGuide/Makefile
           src/WindowsPortGuide/Makefile
           src/ExamplesGuide/Makefile
           src/CodingRulesGuide/Makefile
])

test "x$WITH_PDFLATEX" = x1  && sum_pdflatex=OK  || sum_pdflatex="no * (MANDATORY)"
test "x$WITH_MAKEINDEX" = x1 && sum_makeindex=OK || sum_makeindex="no * (MANDATORY)"
test "x$WITH_BIBTEX" = x1    && sum_bibtex=OK    || sum_bibtex="no * (MANDATORY)"
test "x$WITH_TRALICS" = x1   && sum_tralics=OK   || sum_tralics="no * (OPTIONAL)"
test "x$WITH_LIBXSLT" = x1   && sum_libxslt=OK   || sum_libxslt="no * (OPTIONAL)"

cat <<EOT > summary
(doc)

 Support for          is
 -----------------------------
  pdflatex             ${sum_pdflatex}
  makeindex            ${sum_makeindex}
  bibtex               ${sum_bibtex}
  tralics              ${sum_tralics}
  libxslt              ${sum_libxslt}
EOT
cat summary

cat <<EOT

Congratulations!
Now you can build Open TURNS PDF documentation as usual:
	make
	make check (optional but recommended)
	make install
	make installcheck (optional but recommended)

If you have tralics and libxslt installed, you can also
build the HTML documentation:
	make html
	make install-html

Have fun!
EOT
