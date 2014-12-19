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

        """
        #thetaLast stores value of theta in previous timestep
        self.thetaLast=0;
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']

    def sendCommand(self, cmd):
        """
        Send movement to Sphero.

        Use holonomic drive to get x and y values. Converts these values to v and theta
        to be sent to sphero. Similar to differential drive but here v is always positive
        and use theta rather than angular velocity
        """

        # Extract data
        x = cmd[0]
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
            #sphero turns with no velocity for 0.5 seconds for a sharp turn
            self.SpheroInitHandler.sphero.roll(0,int(theta),1,False)
            time.sleep(0.5)
            self.SpheroInitHandler.sphero.roll(min(100,int(v))*3/2,int(theta),1,False)
            #saves current theta value to compare in next timestep
            self.thetaLast=theta
