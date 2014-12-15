"""
========================================================
SpheroInit.py - Sphero Initialization Handler
========================================================

Initialize the bluetooth and settings
"""
import sphero_driver
import logging
import sys
import time

import lib.handlers.handlerTemplates as handlerTemplates

class SpheroInitHandler(handlerTemplates.InitHandler):
    def __init__(self, executor):
        """
        Initialization handler for Sphero robot.

        sphero.connect: Connects to Sphero's bluetooth
        sphero.set_raw_data_strm: sets rate that Sphero sends sensor data to computer
        sphero.config_collision_detect: sets sensitivity and frequency of collision info
        sphero.add_async_callback: enables callback functions for data and collision info
        """
        self.data_info= {}
        self.sphero = sphero_driver.Sphero()
        self.sphero.connect()
        self.sphero.set_raw_data_strm(100, 1 , 0, False)
        self.sphero.config_collision_detect(1,80,80,80,80,10,False)
        self.sphero.add_async_callback(chr(0x03),self._dataStrmCallBack)
        self.sphero.add_async_callback(chr(0x07),self._collisionCallBack)
        self.sphero.start()

    def _stop(self):
        """
        Shut Sphero down and disconnect bluetooth connection
        """
        self.sphero.roll(0,0,1,False)
        sphero.go_to_sleep(0,0,False)
        self.sphero.shutdown = True
        self.sphero.join()
        self.sphero.disconnect()
        sys.exit(1)
        
    def getSharedData(self):
        return {'SPHERO_INIT_HANDLER': self}
    
    def _collisionCallBack(self, output):
        """
        Determines if Sphero has collided with something

        collision (bool): if there's a collision (default=false)
        """
        self.collision = True
    
    def _dataStrmCallBack(self, output):
        """
        Gets sensor data from sphero and resets collision to false

        collision (bool): if there's a collision (default=false)
        data_info: Stores odometry and velocity values in dictionary
        stopped (bool): determines if Sphero is stationary
        """
        self.collision=False
        self.data_info['ODOM_X'] = output['ODOM_X']
        self.data_info['ODOM_Y'] = output['ODOM_Y']
        self.data_info['VELOCITY_X'] = output['VELOCITY_X']
        self.data_info['VELOCITY_Y'] = output['VELOCITY_Y']
        if ((output['VELOCITY_X'] + output['VELOCITY_Y']) > 20):
            self.stopped=True
        else:
            self.stopped=False
