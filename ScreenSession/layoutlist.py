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

import os
import sys
from util import tmpdir
from ScreenSaver import ScreenSaver

if __name__ == '__main__':
    lltmpdir = os.path.join(tmpdir, '___layoutlist')
    try:
        os.makedirs(lltmpdir)
    except:
        pass
    helper = os.getenv('PYTHONBIN') + ' ' + os.path.join(os.path.split(os.path.abspath(__file__))[0],
            'layoutlist_agent.py')

    session = (sys.argv)[1]
    newlay = (sys.argv)[2] == '1' and True or False
    newwin = (sys.argv)[3] == '1' and True or False
    s_no_end = (sys.argv)[4]
    no_end = (sys.argv)[4] == '1' and True or False
    select_other = (sys.argv)[5] == '1' and True or False
    title_width = int((sys.argv)[6])
    autosearch = (sys.argv)[7]
    layout_checkpoint = (sys.argv)[8] == '1' and True or False

    try:
        height = int((sys.argv)[9])
    except:
        height = 0


    
    ss = ScreenSaver(session)
    if no_end:
        lock_and_com_file = os.path.join(lltmpdir, '%s' %
                session.split('.', 1)[0])
        if os.path.exists(lock_and_com_file):
            try:
                f = open(lock_and_com_file, 'r')
                pid = f.readline().strip()
                tmpwin = f.readline().strip()
                tmplay = f.readline().strip()
                cwin = f.readline().strip()
                if tmpwin != '-1':
                    cwin = ss.get_number_and_title()[0]
                else:
                    cwin = '-1'
                clay = f.readline().strip()
                clay = ss.get_layout_number()[0]
                f.close()
                if layout_checkpoint:
                    from . import layout
                    layout.setup_dirs(session, clay)
                    layout.layout_checkpoint(session, clay)
                f = open(lock_and_com_file, 'w')
                f.write(str(pid) + '\n' + str(tmpwin) + '\n' + str(tmplay) +
                        '\n' + str(cwin) + '\n' + str(clay) + '\n' + str(title_width) +
                        '\n' + str(height))
                f.close()
                from signal import SIGINT
                os.kill(int(pid), SIGINT)
                if tmplay != '-1':
                    ss.command_at(False, 'layout select %s' % tmplay)
                elif tmpwin != '-1':
                    ss.command_at(False, 'select %s' % tmpwin)
            except:
                pass
            else:
                sys.exit(0)

    (currentlayout, currentlayoutname) = ss.get_layout_number()
    if layout_checkpoint:
        from . import layout
        layout.setup_dirs(session, currentlayout)
        layout.layout_checkpoint(session, currentlayout)
    if newlay:
        if ss.get_layout_new('LAYOUTLIST'):
            ss.screen('-t layoutlist %s %s %s %s 1 1 %s %s %s %s' % (helper,
                      session, None, currentlayout, s_no_end,
                      title_width, autosearch, height))
        else:
            curwin = ss.get_number_and_title()[0]
            ss.screen('-t layoutlist %s %s %s %s 1 0 %s %s %s %s' % (helper,
                      session, curwin, currentlayout, s_no_end,
                      title_width, autosearch, height))
    elif newwin:
        curwin = ss.get_number_and_title()[0]
        ss.screen('-t layoutlist %s %s %s %s 1 0 %s %s %s %s' % (helper,
                  session, curwin, currentlayout, s_no_end, title_width,
                  autosearch, height))
    else:
        from . import layoutlist_agent
        layoutlist_agent.MAXTITLELEN = title_width
        layoutlist_agent.NO_END = no_end
        layoutlist_agent.AUTOSEARCH_MIN_MATCH = int(autosearch)
        sys.exit(layoutlist_agent.run(session, False, False, None,
                 currentlayout, height, select_other))

