#!/usr/bin/env python
# file: screen-display-regions.py
# author: Artur Skonecki
# website http://adb.cba.pl
# description: script for GNU Screen reassembling functionality of tmux display-panes + swap regions + rotate regions

import sys,os,subprocess,time,signal,tempfile,pwd,copy
from util import tmpdir
import GNUScreen as sc
from ScreenSaver import ScreenSaver

logfile="__log-regions"
inputfile="__scs-regions-input-%d"%(os.getpid())
subprogram='screen-session-primer'
subprogram_args='-nh'

def local_copysign(x, y):
    "Return x with the sign of y. Backported from Python 2.6."
    if y >= 0:
        return x * (1 - 2 * int(x < 0))
    else:
        return x * (1 - 2 * int(x >= 0))

def rotate_list(l, offset):
    """
    Rotate a list by (offset) elements. Elements which fall off
    one side are provided again on the other side.
    Returns a rotated copy of the list. If (offset) is 0,
    returns a copy of (l).
    
    Examples:
        >>> rotate_list([1, 2, 3, 4, 5, 6], 2)
        [3, 4, 5, 6, 1, 2]
        >>> rotate_list([1, 2, 3, 4, 5, 6], -2)
        [5, 6, 1, 2, 3, 4]
    """
    if len(l) == 0:
        raise ValueError("Must provide a list with 1 or more elements")
    if offset == 0:
        rv = copy.copy(l)
    else:
        real_offset = offset % int(local_copysign(len(l), offset))
        rv = (l[real_offset:] + l[:real_offset])
    return rv


def handler(signum,frame):
    global win_history
    bSelect=False
    mode=-1
    f=open(inputfile,'r')
    ch=f.readline().strip()
    f.close()
    try:
        number=int(ch[1:])
    except:
        number=0
        

    os.remove(inputfile)
    if ch[0]=='s':
        mode=1
    elif ch[0]=='S':
        mode=1
        bSelect=True
    elif ch[0]=="'" or ch[0]=='g' or ch[0]=='G':
        mode=0
        bSelect=True
    elif ch[0]=="l":
        mode=2
        rnumber=-1*number
    elif ch[0]=="L":
        mode=2
        rnumber=-1*number
        bSelect=True
    elif ch[0]=="r":
        rnumber=number
        mode=2
    elif ch[0]=="R":
        rnumber=number
        mode=2
        bSelect=True
    else:
        mode=0

    
    if number!=-1 and mode==1:
        tmp=win_history[0]
        win_history[0]=win_history[number]
        win_history[number]=tmp
    elif mode==2:
        win_history=rotate_list(win_history,rnumber)

    cleanup()

    if number!=-1 and bSelect:
        if(number!=0 and number<regions_c):
            command='screen -S %s -X eval'%session
            for i in range(0,number):
                command+=' "focus"'
            os.system(command)
    sys.exit(0)

def cleanup():
    print('restoring windows '+str(win_history))
    for i,w in enumerate(win_history):
        scs.select(w)
        scs.kill(wins[i])
        scs.focus()
    scs.focusminsize(focusminsize)
    try:
        os.remove(inputfile)
    except:
        pass


def prepare_windows(scs):
    this_win_history=[]
    new_windows=[]
    i=0
    win=scs.number()
    while True:
        this_win_history.append(win)
        scs.screen('-t scs-regions-helper %s %s %s %d'%(subprogram,subprogram_args,inputfile,i))
        i+=1
        new_windows.append(scs.number())
        scs.focus()
        win=scs.number()
        if win==new_windows[0]:
            break
        
    return this_win_history,new_windows,len(this_win_history)


if __name__=='__main__':
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    logfile=os.path.join(tmpdir,logfile)
    inputfile=os.path.join(tmpdir,inputfile)
    file=os.path.join(tmpdir,logfile)
    sys.stdout=open(logfile,'w')
    sys.stderr=sys.stdout
    subprogram=os.path.join(os.path.dirname(sys.argv[0]),subprogram)

    session=sys.argv[1]
    scs=ScreenSaver(session)
    focusminsize=scs.focusminsize()
    scs.focusminsize('0 0')

    win_history,wins,regions_c=prepare_windows(scs)
    print('helper windows '+str(wins))

    signal.signal(signal.SIGUSR1,handler)
    time.sleep(10)

    cleanup()


