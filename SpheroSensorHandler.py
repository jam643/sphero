"""
==================================================
SpheroSensor.py - Sphero Sensor Handler 
==================================================
"""
import lib.handlers.handlerTemplates as handlerTemplates

class SpheroSensorHandler(handlerTemplates.SensorHandler):
    def __init__(self, executor, shared_data):
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']
        
    def collision(self,initial=False):
        """
        Use Sphero's internal collision detection defined in InitHandler
        """
        if initial:
            self.SpheroInitHandler.collision = False
            return self.SpheroInitHandler.collision
        else:
            return self.SpheroInitHandler.collision
    def stopped(self,initial=False):
        """
        Use sphero's interal odometer to determine if Sphero is stationary
        defined in InitHandler
        """
        if initial:
            self.SpheroInitHandler.stopped = False
            return self.SpheroInitHandler.stopped
        else:
            return self.SpheroInitHandler.stopped


