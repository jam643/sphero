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

        In order to recieve the data packets sent from Sphero to sphero_driver.py,
        callback functions are required to output the data.
        There are two callback functions. dataStrmCallBack gets called several
        times a second with general data from Sphero's sensors.
        collisionCallBack gets called whenever sphero collides with something.
        The two async functions assigns the datatypes of the packets sent to
        sphero_driver.py with the respective callback functions in this handler.
        """
        self.data_info= {}
        self.sphero = sphero_driver.Sphero()
        #sphero.connect Connects to Sphero's bluetooth
        self.sphero.connect()
        #sphero.set_raw_data_strm sets rate that Sphero sends sensor data to computer
        self.sphero.set_raw_data_strm(100, 1 , 0, False)
        #sphero.config_collision_detect sets sensitivity and frequency of collision info
        self.sphero.config_collision_detect(1,80,80,80,80,10,False)
        #sphero.add_async_callback assigns data type of streaming data to a callback fn
        self.sphero.add_async_callback(chr(0x03),self._dataStrmCallBack)
        #sphero.add_async_callback assigns data type of collision to a callback fn
        self.sphero.add_async_callback(chr(0x07),self._collisionCallBack)
        self.sphero.start()

    def _stop(self):
        """
        Shut Sphero down and disconnect bluetooth connection
        """
        self.sphero.roll(0,0,1,False)
        self.sphero.go_to_sleep(0,0,False)
        self.sphero.shutdown = True
        self.sphero.join()
        self.sphero.disconnect()
        sys.exit(1)
        
    def getSharedData(self):
        return {'SPHERO_INIT_HANDLER': self}
    
    def _collisionCallBack(self, output):
        """
        Gets called if sphero collides with something

        output (dict): info at instant of collision such as odometry, velocity, and timestamp values
        """
        
        #collision set to true if there's a collision and set false for datastream callback
        self.collision = True
    
    def _dataStrmCallBack(self, output):
        """
        Gets called several times a second and outputs sensor data from sphero and resets collision to false

        output (dict): info inludes odometry, velocity, quaternion, accelerometer, and gyroscope values
        """
        #reset collision to false
        self.collision=False
        self.data_info['ODOM_X'] = output['ODOM_X']
        self.data_info['ODOM_Y'] = output['ODOM_Y']
        self.data_info['VELOCITY_X'] = output['VELOCITY_X']
        self.data_info['VELOCITY_Y'] = output['VELOCITY_Y']
        #stopped (bool) set to true if Sphero is stationary and false if not
        if ((output['VELOCITY_X'] + output['VELOCITY_Y']) > 20):
            self.stopped=False
        else:
            self.stopped=True
