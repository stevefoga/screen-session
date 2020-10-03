#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    find_file.py : find open files in windows
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
import tools

session = (sys.argv)[1]
files = (sys.argv)[2:]

pids = tools.find_files_in_pids(files)
try:
    pids = list(map(int, pids))
    for (win, title) in tools.find_pids_in_windows(session, tools.require_dumpscreen_window(session,
            False), pids):
        print("%s %s" % (win, title))
except:
    pass
