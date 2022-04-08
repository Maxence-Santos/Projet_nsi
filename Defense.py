import rsk
from math import pi, sqrt,radians
from metrics import *

d = False

def pos_def(pos_balle,pos_robot_adv,robot):
    pos_robot = robot.position
    if abs(pos_robot_adv[0] - pos_balle[0]) < 0.12:
        if not d:
            a = sum(list(get_theta_def(pos_balle,"g"))) / 2
            robot.goto((pos_balle[0] - 0.05,pos_balle[1] - 0.05,a))
        
        else:
            a = sum(list(get_theta_def(pos_balle,"d"))) / 2
            robot.goto((pos_balle[0],pos_balle[1],a))
