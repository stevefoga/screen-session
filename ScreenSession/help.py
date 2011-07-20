﻿#!/usr/bin/env python2
#
#    help.py : screen-session help system
#
#    Copyright (C) 2010-2011 Artur Skonecki
#
#    Authors: Artur Skonecki <admin [>at<] adb.cba.pl>
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

VERSION='git'
version_str="screen-session (%s) - a collection of tools for GNU Screen."%VERSION

'''
broken/unfinished tools:
    grab  - grab a process and attach it to current tty\n\
          (requires injcode)\n\
    sort  - sort windows by title\n\
    manager-remote -

Unpractical/useless tools:
    find-pid  - find PIDs in windows (greping dump tool output is better)\n\
'''


help_help="\
Usage:   screen-session [mode] [options]\n\
\n\
A collection of utilities for GNU Screen.\n\
\n\
Help:    scs help [mode]\n\
\n\
Options supported by all tools:\n\
    -S [target] - target Screen session name, \".\" denotes the current session\n\
    --help      - print detailed mode's help\n\
\n\
Environment variables:\n\
    SCREENPATH  - determines GNU Screen executable path\n\
    PYTHONBIN   - Python interpreter path\n\
\n\
Session saver modes:\n\
    save        - save a session\n\
    load        - load a session from a save file\n\
    ls          - list saved sessions\n\
\n\
Other tools:\n\
    dump        - print informations about windows in the session\n\
    find-file   - find open files in windows\n\
    group       - move windows to a group\n\
    kill        - send a signal to the last process started in a window\n\
    kill-group  - recursively kill a group and all windows inside\n\
    kill-zombie - kill all zombie windows in the session\n\
    layoutlist  - display a browseable list of layouts in the session\n\
    manager     - a sessions manager with a split Screen window preview\n\
    name        - get or set the sessionname\n\
    nest-layout - nest a layout in the current region\n\
    new-window  - open a new Screen window with the same working directory\n\
    regions     - display a number in each region (tmux display-panes)\n\
    renumber    - renumber windows to fill the gaps\n\
    subwindows  - print windows contained in a group\n\
\n\
Please report bugs to http://github.com/skoneka/screen-session/issues\
"

help_regions="Usage: screen-session regions [options]\n\
       scs r\n\
       :bind X at 0 exec scs regions\n\
\n\
Display a number in each region.\n\
Allows selecting, swapping and rotating. Inspired by tmux display-panes.\n\
Requires an active layout.\n\
\n\
Keys:\n\
goto region  - number and [g] or ['] or [space]\n\
swap regions - number and [s]\n\
rotate left  - number and [l]\n\
rotate right - number and [r]\n\
\n\
reverse goto region     - number and [G]\n\
swap regions and select - number and [S]\n\
rotate left  and select - number and [L]\n\
rotate right and select - number and [R]\
"

help_kill="Usage: screen-session kill [options] [signal=TERM] [window=current]\n\
       scs K\n\
\n\
Kill last process started in a window.\n\
Useful for closing random emacs/vim instances and hung up ssh clients.\n\
For a list of signal names run: $ pydoc signal\n\
WARNING: sending SIGKILL to the current window may crash Screen\
"

help_kill_zombie="Usage: screen-session kill-zombie [options] [group_ids]\n\
       scs kz\n\
\n\
Kill all zombie windows in session. Optionally specify target groups.\
"

help_kill_group="Usage: screen-session kill-group [options] [groupNum0] [groupNum..]\n\
       scs kg\n\
\n\
Recursively kill groups and windows inside.\n\
Accepts titles and window numbers as arguments.\n\
A dot \".\" selects current window, 2 dots \"..\"  select current group.\n\
Take extra care with this command.\
"

help_new_window='Usage: screen-session new-window [options] [program]\n\
       scs new\n\
       scs nw\n\
       :bind c eval "colon" "stuff \\"at 0 exec scs new-window \\""\n\
\n\
Start a new Screen window with the same working directory as the current window.\n\
It also sets new window number to current number + 1.\n\
\n\
Options:\n\
-d [directory] - specify the new window working directory\
'

help_dump="Usage: screen-session dump [options] [window_ids]\n\
       scs d\n\
\n\
Print informations about windows in session (MRU order by default).\n\
A dot \".\" selects current window, 2 dots \"..\"  select current group.\n\
\n\
Options:\n\
-P   - do not show pid data\n\
-r   - reverse the output\n\
-s   - sort by window number\
"

help_find_pid="Usage: screen-session find-pid [options] [PIDs]\n\
       scs fp\n\
\n\
Find PIDs in windows.\n\
Example: screen-session find-pid $(pgrep vim)\
"

help_find_file="Usage: screen-session find-file [options] [files]\n\
       scs ff\n\
\n\
Find open files in windows. Requires lsof.\n\
\n\
Example:\n\
tail -f /var/log/dmesg\n\
scs find-file /var/log/dmesg\
"

_help_grab="Grab a process and attach to the current tty.\n\
Works with applications without complicated output scheme.\n\
A simple demonstration of injcode tool by Thomas Habets.\n\
http://blog.habets.pp.se/2009/03/Moving-a-process-to-another-terminal\n\
\nUsage: screen-session grab [PID]\n\
and on the previous shell type:\n\
$ disown\n\
It works more reliably if commands from the script are typed manually."

help_group='Usage: screen-session group [options] [GROUP] [windows]\n\
       scs g\n\
       :bind G eval "colon" "stuff \\"at 0 exec scs group \\""\n\
\n\
Move windows to a group.\n\
If no windows given, move the current window.\
'

#help_manager="Usage: screen-session manager [options]\n\
help_manager="Usage: screen-session manager [account@host]\n\
       scs m\n\
\n\
Sessions manager for GNU Screen with preview in a split window.\n\
Requires python 2.5+\n\
\n\
KEYS:\n\
CTRL + g  - default escape key\n\
ALT + t   - toggle between regions\n\
ALT + e   - step into a selected session\n\
ALT + q   - quit\n\
Alt + w   - wipe\n\
\n\
COMMANDS:\n\
? or h          - display help\n\
q[uit]          - exit session manager\n\
e[nter]         - enter into a session\n\
a[ttach] [name] - attach and select\n\
d[etach] [name] - detach and deselect\n\
n[ame] [name]   - rename\n\
s[creen] [args] - create session\n\
save [output]   - save session\n\
w[ipe]          - wipe dead sessions\n\
restart         - restart session manager\n\
r[efresh]       - refresh session list\n\
l[ayout]        - toggle layout\n\
kill K          - kill selected session\n\
"

_help_manager_remote="Usage: screen-session manager-remote\n\
\n\
Sessions manager for GNU Screen with preview in a split window and\n\
support for multiple hosts. Requires python 2.5+\
"

help_nest='Usage: screen-session nest-layout [options] [TARGET_LAYOUT]\n\
       scs nl\n\
       :bind N eval "colon" "stuff \\"at 0 exec scs nest-layout \\""\n\
\n\
Nest a layout in the current region.\
'

help_layoutlist='Usage: screen-session layoutlist [options] [HEIGHT]\n\
       scs ll\n\
       :bind l at 0 exec scs layoutlist -l -c 20\n\
\n\
Displays a browseable list of layouts. There are two list creation algorithms.\n\
If HEIGHT != 0, an alternative list creation algorithm is used. Layout numbers\n\
are modulo divided by HEIGHT and the reminder determines their Y position.\n\
This tool comes handy after raising MAXLAY in "screen/src/layout.h"\n\
\n\
Options:\n\
-l              - create a temporary layout and window for layoutlist\n\
-w              - create a temporary window for layoutlist\n\
-t [width=11]   - set title width\n\
-a [min_len=2]  - minimum matching charecters for auto highlight,\n\
                  min_len = 0 disables auto highlight\n\
-c              - do not terminate layoutlist after selecting a layout\n\
                  or reselect a running layoutlist, best used with "-l" option,\n\
                  there should be running only one layoutlist started with "-c"\n\
                  per session\n\
\n\
Keys:\n\
?               - display help\n\
ENTER           - confirm / select\n\
ARROWS and hjkl - movement\n\
/ or SPACE      - start searching layout titles\n\
n and p         - next / previous search result\n\
NUMBER          - move to a layout\n\
r or C-c or C-l - refresh the layout list\n\
m or a          - toggle MRU view,\n\
v               - toggle search/autohighlight results view\n\
o               - toggle current and selected layout\n\
q               - quit / select previous layout\n\
Q               - force quit if "-c" option was used\
'

help_renumber="""Usage: screen-session renumber [options]\n\
\n\
Renumber windows to fill the gaps.\n\
Use case: suppose you are trying to run ":at 0 some_command" but there is\n\
         no such window.
"""

_help_sort="Usage: screen-session sort [options]\n\
\n\
Sort windows by titles.\
"

help_subwindows="Usage: screen-session subwindows [groupids or titles]\n\
       scs sw\n\
\n\
Print windows contained in groups.\n\
A dot \".\" selects current window, 2 dots \"..\"  select current group.\
"

help_name="Usage: screen-session name [options] [new_sessionname]\n\
       scs n\n\
\n\
Get or set the sessionname.\
"
help_saver_other="Usage: screen-session other [options] \n\
\n\
Auxiliary mode, used mainly by screen-session-primer.\n\
\n\
Options:\n\
--pack [target]\n\
    archive unpacked savefile ( which must be accessible from --dir )\n\
--unpack [savefile]\n\
    unpack savefile to /tmp/screen-session-$USER\n\
-l --log  [file]\n\
    output to a file instead of stdout\n\
-d --dir  [directory = $HOME/.screen-sessions]\n\
    directory holding saved sessions\
"

help_saver_ls="Usage: screen-session save [-S sessionname] [options] [savefile_filter]\n\
\n\
List saved sessions.\n\
\n\
Options:\n\
-l --log  [file]\n\
    output to a file instead of stdout\n\
-d --dir  [directory = $HOME/.screen-sessions]\n\
    directory holding saved sessions\
"

help_saver_save="Usage: screen-session save [-S sessionname] [options] [target_savefile]\n\
       :bind S at 0 exec screen -mdc /dev/null screen-session save -H SECURE -f -S $PID.$STY\n\
\n\
Save GNU Screen and VIM sessions to a file.\n\
\n\
Options:\n\
-f --force\n\
    force saving even if a savefile with the same name already exists\n\
-e --exclude  [windows]\n\
    a comma separated list of windows to be ignored during saving,\n\
    if a window is a group all nested windows are also included\n\
-L --exclude-layout  [layouts]\n\
    a comma separated list of layouts to be ignored during saving,\n\
-H --no-scroll  [windows]\n\
    a comma separated list of windows which scrollbacks will be ignored,\n\
    if a window is a group all nested windows are also included,\n\
    using keyword \"all\" affects all windows\n\
-y --no-layout\n\
    disable layout saving\n\
-V --no-vim\n\
    disable vim session saving\n\
-l --log [file]\n\
    output to a file instead of stdout\n\
-d --dir  [directory = $HOME/.screen-sessions]\n\
    directory holding saved sessions\n\
\n\
Examples:\n\
#1# save Screen named SESSIONNAME as mysavedsession\n\
screen-session save -S SESSIONNAME mysavedsession\n\
#2# save the current session, force overwrite of old savefiles\n\
scs save --force\n\
#3# save the current session without layouts\n\
scs save --no-layout\n\
#4# run session saver after 3 minutes of inactivity, exclude group SECURE\n\
:idle 180 at 0 exec scs save --no-scroll SECURE --force --log /dev/null\n\
#5# a binding which works after changing the sessioname\n\
bind S eval 'colon' 'stuff \"at 0 exec screen -mdc /dev/null scs save -H SECURE -f -S \\\"$PID.$STY\\\"\"^M'\
"

help_saver_load="Usage: screen-session load [-S sessionname] [options] [source_savefile]\n\
\n\
Load saved session from a file.\n\
\n\
Options:\n\
-x --exact\n\
    load session with the same window numbers, move existing windows,\n\
    to OTHER_WINDOWS group and delete existing layouts\n\
-X --exact-kill\n\
    same as exact, but also kill all existing windows\n\
-F --force-start  [windows]\n\
    a comma separated list of windows which will start programs immediately,\n\
    using keyword \"all\" causes all loaded windows to start their subprograms\n\
    without waiting for user's confirmation\n\
-y --no-layout\n\
    disable layout loading\n\
-n --no-group-wrap\n\
    do not wrap windows in RESTORE_* or OTHER_WINDOWS_* groups\n\
-m --no-mru\n\
    disable restoring of the Most Recently Used order of windows\n\
-l --log  [file]\n\
    output to a file instead of stdout\n\
-d --dir  [directory = $HOME/.screen-sessions]\n\
    directory holding saved sessions\n\
\n\
Examples:\n\
#1# restore mysavedsession inside Screen named SESSIONNAME\n\
screen-session load -S SESSIONNAME --exact mysavedsession\n\
#2# load the last saved session inside the current Screen session\n\
scs load\n\
#3# load the last saved session with exactly the same window numbers\n\
scs load --exact\n\
#4# load the last saved session inside the current session without layouts\n\
scs load --no-layout\n\
#5# load the last saved session into a new Screen\n\
screen -m scs load --exact-kill\
"

def run(argv):
    if False:
        print(help_regions)
        print(help_kill_zombie)
        print(help_kill_cgroup)
        print(help_new_window)
        print(help_dump)
        print(help_grab)
        print(help_group)
        print(help_manager)
        print(help_nest)
        print(help_renumber)
        print(help_sort)
        print(help_name)
        print(help_saver_modes)

    try:
        mode=argv[1]
    except:
        mode='help'
    try:
        if mode in ('help','h'):
            #print(version_str+'\n')
            print(help_help)
        elif mode=='--version':
            print(version_str)
        elif mode in ('regions','r'):
            print(help_regions)
        elif mode in ('kill','K'):
            print(help_kill)
        elif mode in ('kill-zombie','kz'):
            print(help_kill_zombie)
        elif mode in ('kill-group','kg'):
            print(help_kill_group)
        elif mode in ('dir','new','new-window','nw'):
            print(help_new_window)
        elif mode in ('dump','d'):
            print(help_dump)
        elif mode in ('find-pid','fp'):
            print(help_find_pid)
        elif mode in ('find-file','ff'):
            print(help_find_file)
        elif mode=='grab':
            print(help_grab)
        elif mode in ('group','g'):
            print(help_group)
        elif mode in ('manager','m'):
            print(help_manager)
        elif mode in ('manager-remote','mr'):
            print(help_manager_remote)
        elif mode in ('nest','nest-layout','nl'):
            print(help_nest)
        elif mode in ('layoutlist','ll'):
            print(help_layoutlist)
        elif mode=='renumber':
            print(help_renumber)
        elif mode=='sort':
            print(help_sort)
        elif mode in ('subwindows','sw'):
            print(help_subwindows)
        elif mode in ('name','n'):
            print(help_name)
        elif mode=='ls':
            print(help_saver_ls)
        elif mode=='save':
            print(help_saver_save)
        elif mode=='load':
            print(help_saver_load)
        elif mode=='other':
            print(help_saver_other)
        else:
            print('No help for mode: %s'%mode)
            return 1
    except IOError:
        pass
    return 0

if __name__=='__main__':
    import sys
    sys.exit(run(sys.argv))

