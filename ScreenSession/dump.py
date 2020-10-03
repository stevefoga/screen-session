#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    dump.py : print informations about windows in the session
#
#    Copyright (C) 2010-2011 Artur Skonecki http://github.com/skoneka
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from . import GNUScreen as sc
from .ScreenSaver import ScreenSaver
from . import tools
from . import util 

if __name__ == '__main__':
    session = (sys.argv)[1]
    showpid = (sys.argv)[2]
    reverse = (sys.argv)[3]
    sort = (sys.argv)[4]
    windows = util.expand_numbers_list((sys.argv)[5:])

    if showpid == '0':
        showpid = False
    else:
        showpid = True
    if reverse == '0':
        reverse = True
    else:
        reverse = False
    if sort == '0':
        sort = False
    else:
        sort = True
    ss = ScreenSaver(session)
    tools.dump(ss, tools.require_dumpscreen_window(session, True),
               showpid, reverse, sort, windows)
    tools.cleanup()

