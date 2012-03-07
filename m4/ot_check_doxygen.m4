#                                               -*- Autoconf -*-
#
#  ot_check_doxygen.m4
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
#  Id:      $Id: ot_check_doxygen.m4 1539 2012-02-27 13:48:06Z schueller $
#
#
#  This file is intended to be include in the configure.in file
#  of Open TURNS project to check whether Doxygen is available on the
#  build platform.
#
# OT_CHECK_DOXYGEN
# ----------------
#
AC_DEFUN([OT_CHECK_DOXYGEN],
[
  WITH_DOXYGEN=0
  AC_ARG_VAR([DOXYGEN], [path for Doxygen tool])
  AC_PATH_PROG([DOXYGEN], [doxygen])
  test x$DOXYGEN = x || WITH_DOXYGEN=1

  # Propagate test into Makefiles
  AM_CONDITIONAL(WITH_DOXYGEN, test $WITH_DOXYGEN = 1)
])
