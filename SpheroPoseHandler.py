#!/usr/bin/env python
"""
=======================================
SpheroPoseHandler.py - 2D Pose provider for sphero
=======================================
"""

import lib.handlers.handlerTemplates as handlerTemplates

class SpheroPoseHandler(handlerTemplates.PoseHandler):
    def __init__(self, executor, shared_data):
        """
        Pose Handler for Sphero
        """
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']
        self.x=0
        self.y=0
        self.angle=0
        

    def getPose(self, cached=False):
        """ Returns the most recent (x,y,theta) reading from sphero """
        self.x=self.SpheroInitHandler.data_info['ODOM_X']
        self.y=self.SpheroInitHandler.data_info['ODOM_Y']
        return ([self.x, self.y, self.angle])

        

