#                                               -*- Autoconf -*-
#
#  ot_check_tralics.m4
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
#
#  This file is intended to be include in the configure.in file
#  of Open TURNS project to check whether Bc is available on the
#  build platform.
#
# OT_CHECK_TRALICS
# -----------
#
AC_DEFUN([OT_CHECK_TRALICS],
[
  WITH_TRALICS=0
  AC_ARG_VAR([TRALICS], [path for tralics tool])
  AC_PATH_PROG([TRALICS], [tralics])
  test x$TRALICS = x || WITH_TRALICS=1

  # Option --with-tralics-confdir=/some/where
  TRALICS_CONFDIR=/usr/share/tralics/confdir
  AC_ARG_WITH(
    tralics-confdir,
  AC_HELP_STRING(
    [--with-tralics-confdir=directory],
    [tralics's configuration directory]),
  [ if test "$withval" != "no" -a \
            "$withval" != "yes"; then
      TRALICS_CONFDIR="$withval"
    fi
  ])
  test -f $TRALICS_CONFDIR/latex.plt || WITH_TRALICS=0

  # Propagate test into atlocal
  AC_SUBST(WITH_TRALICS)

  # Propagate configuration directory
  AC_SUBST(TRALICS_CONFDIR)

  # Propagate test into Makefiles
  AM_CONDITIONAL(WITH_TRALICS, test $WITH_TRALICS = 1)
])
