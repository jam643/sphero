InitHandler: #Robot default init handler with default argument values
sphero.SpheroInitHandler()

MotionControlHandler: # Robot default locomotion command handler with default argument values
share.MotionControl.VectorControllerHandler()

LocomotionCommandHandler: # Robot default locomotion command handler with default arguement values
sphero.SpheroLocomotionCommandHandler()

DriveHandler: # Robot default drive handler with default argument values
share.Drive.HolonomicDriveHandler(multiplier=50.0,maxspeed=999.0)

PoseHandler: # Robot default pose handler with default argument values
share.Pose.NullPoseHandler(initial_region='Classroom1')


RobotName: # Robot Name
Sphero

Type: # Robot type
sphero

SensorHandler: # Robot Default sensor handler with default argument values
sphero.SpheroSensorHandler()

ActuatorHandler: # Robot default actuator handler with default argument values
sphero.SpheroActuatorHandler()