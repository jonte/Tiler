#!/usr/bin/env python
import commands, sys, os
class Positions:
    N   = 0
    S   = 1
    W   = 2
    E   = 3
    SW  = 4
    NE  = 5
    NW  = 6
    SE  = 7

class WMHelpers:
    xprop = "xprop"
    
    def getCurrentWindowID(self):
        cmdStr = "%s -root _NET_ACTIVE_WINDOW" % self.xprop
        s = commands.getoutput(cmdStr)
        try:
            (_,_,_,_, id) = s.split(" ")
            return id
        except ValueError:
            print "Can't run %s" % cmdStr
            sys.exit()
    
    # Only tested on one screen..
    # Returns a tuple of (x,y) containing the resolution
    def _getResolution(self):
        cmdStr = "xdpyinfo | grep dimensions"
        try:
            r = [x for x in commands.getoutput(cmdStr).split(" ") 
                         if x != '']
            (_,res,_,_,_) = r
            w,h = res.split("x")
            return (int(w),int(h))
        except ValueError:
            print "Can't run %s" % cmdStr

    # Move the specified window (specced using X window IDs) to the location
    # specified by position (of type Position.x)
    def positionWindow(self, window, position):
        w,h = self._getResolution()
        cmdStr = "wmctrl -i -r %s -e 1,%s,%s,%s,%s"

        if position == Positions.W:
            os.system(cmdStr % (window, 0,0,w/2,h))
        if position == Positions.E:
            os.system(cmdStr % (window, w/2,0,w/2,h))

class Tiler:
    def __init__(self):
        self.wmhelpers = WMHelpers()

    def run(self, position):
        try:
            ipos = eval("Positions."+position)
        except AttributeError:
            print "No such position"
            sys.exit()
        currentWindow = self.wmhelpers.getCurrentWindowID()
        self.wmhelpers.positionWindow(currentWindow, ipos)

        

if __name__ == "__main__":
    t = Tiler()
    t.run(sys.argv[1])
