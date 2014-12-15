"""
==================================================
SpheroSensor.py - Sphero Sensor Handler 
==================================================
"""
import lib.handlers.handlerTemplates as handlerTemplates
import logging

class SpheroSensorHandler(handlerTemplates.SensorHandler):
    def __init__(self, executor, shared_data):
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']
        
    def collision(self,initial=False):
        """
        Use Sphero's internal collision detection

        collision (bool): true if sphero has collided with something
        """
        if initial:
            self.SpheroInitHandler.collision = False
            return self.SpheroInitHandler.collision
        else:
            return self.SpheroInitHandler.collision
    def stopped(self,initial=False):
        """
        Use sphero's interal odometer to determine if Sphero is stationary

        stopped (bool): true if sphero has stopped moving
        """
        if initial:
            self.SpheroInitHandler.stopped = False
            return self.SpheroInitHandler.stopped
        else:
            return self.SpheroInitHandler.stopped


