from robomaster import robot
import time

if name == 'main':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    '''
    x = x-axis movement distance,( meters) [-5,5]
    y = y-axis movement distance,( meters) [-5,5]
    z = rotation about z axis ( degree)[-180,180]
    xy_speed = xy axis movement speed,( unit meter/second) [0.5,2]
    '''
    ep_chassis.move(x=2.6, y=0, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=45, xy_speed=1).wait_for_completed()
    ep_chassis.move(x=3.5, y=0, z=0, xy_speed=.75).wait_for_completed()
    ep_chassis.move(x=0, y=-0.3, z=0, xy_speed=.75).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=50, xy_speed=.75).wait_for_completed()
    ep_chassis.move(x=.2, y=0, z=0, xy_speed=.75).wait_for_completed()
    ep_robot.close()