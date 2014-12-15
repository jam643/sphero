#!/usr/bin/env python
"""
==================================================================
SpheroLocomotionCommand.py - Sphero Locomotion Command Handler
==================================================================

Send velocity and theta commands to Sphero.
"""

import lib.handlers.handlerTemplates as handlerTemplates
import math
import time

class SpheroLocomotionCommandHandler(handlerTemplates.LocomotionCommandHandler):
    def __init__(self, executor, shared_data):
        """
        Locomotion Command handler for Sphero robot.

        thetaLast (int): theta value in previous time step
        """
        self.thetaLast=0;
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']

    def sendCommand(self, cmd):
        """
        Send movement to Sphero. 
        """

        # Extract data
        x = -cmd[0]
        y = cmd[1]
        #convert x and y to v and theta values
        v=math.sqrt(x**2+y**2)
        theta=math.atan2(x,y)*180/math.pi
        if (theta<0):
            theta+=360
        # Call robot movement, if sphero has a sharp turn, stop for a bit while turning
        if(abs(theta-self.thetaLast)<135 or abs(theta-self.thetaLast)>225):
            self.SpheroInitHandler.sphero.roll(min(100,int(v))*3/2,int(theta),1,False)
        else:
            self.SpheroInitHandler.sphero.roll(0,int(theta),1,False)
            time.sleep(0.5)
            self.SpheroInitHandler.sphero.roll(min(100,int(v))*3/2,int(theta),1,False)
        self.thetaLast=theta
