"""
=====================================================
SpheroActuator.py - Sphero Actuator Handler
=====================================================
"""
import lib.handlers.handlerTemplates as handlerTemplates
import logging

class SpheroActuatorHandler(handlerTemplates.ActuatorHandler):
    def __init__(self, executor, shared_data):
        self.SpheroInitHandler = shared_data['SPHERO_INIT_HANDLER']
        try:
            self.loco = executor.hsub.getHandlerInstanceByType(handlerTemplates.LocomotionCommandHandler)
        except NameError:
            print "(ACT) Locomotion Command Handler not found."
            exit(-1)

        self.angle = 0
        
    def turnLEDOn(self, red, green, blue, actuatorVal, initial=False):
        """
        Use Sphero's LED

        red (int): red color of the led
        green (int): green color of the led
        blue (int): blue color of the led
        """
        if initial:
            pass
            
        else:
            if actuatorVal:
                self.SpheroInitHandler.sphero.set_rgb_led(red, green, blue, 0, False)
            else:
                self.SpheroInitHandler.sphero.set_rgb_led(0,0,0,0,False)

    def turnBackLEDOn(self, actuatorVal, initial=False):
        """
        Use Sphero's back LED to indicate heading
        """
        if initial:
            pass
            
        else:
            if actuatorVal:
                self.SpheroInitHandler.sphero.set_back_led(200,False)
            else:
                self.SpheroInitHandler.sphero.set_back_led(0,False)


    def move(self, v, actuatorVal, initial=False):
        """
        Sphero moves forward at velocity v

        v (int): velocity 0-255
        """
        if initial:
            pass
            
        else:
            if actuatorVal:
                self.loco.sendCommand([v,self.angle])
            else:
                self.loco.sendCommand([0,self.angle])

    def turn(self, angle, actuatorVal, initial=False):
        """
        turn with angle, + for ccw

        angle (int): angle to turn
        """
        if initial:
            pass
            
        else:
            if actuatorVal:
                self.angle += angle
                self.angle = self.angle%360
                self.loco.sendCommand([0,self.angle])
            else:
                self.loco.sendCommand([0,self.angle])
    
