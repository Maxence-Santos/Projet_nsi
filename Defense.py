import rsk
from math import pi, sqrt,radians
from metrics import *

d = 0

def pos_def(pos_balle,pos_robot_adv,pos_goal,robot):
    pos_robot_x = (pos_balle[0] + pos_goal[0]) / 2
    pos_robot_y = (pos_balle[1] + pos_goal[1]) / 2
    if abs(pos_robot_adv[0] - pos_balle[0]) < 0.15 and abs(pos_robot_adv[1] - pos_balle[1] < 0.03):
        if not d and pos_balle[1] >= 0 and pos_balle[0] < 0:
            a = sum(list(get_theta_def(pos_balle,"g"))) / 2
            robot.goto((pos_robot_x + 0.2,pos_robot_y - 0.1,a))
        elif not d and pos_balle[1] < 0 and pos_balle[0] < 0:
            a = sum(list(get_theta_def(pos_balle,"g"))) / 2
            robot.goto((pos_robot_x + 0.2,pos_robot_y + 0.1,a))
        
        else:
            if d and pos_balle[1] >= 0 and pos_balle[0] >= 0:
                a = sum(list(get_theta_def(pos_balle,"d"))) / 2
                robot.goto((pos_robot_x - 0.2,pos_robot_y - 0.1,a))
            elif d and pos_balle[1] < 0 and pos_balle[0] >= 0:
                a = sum(list(get_theta_def(pos_balle,"d"))) / 2
                robot.goto((pos_robot_x - 0.2,pos_robot_y + 0.1,a))
    
    else:
        robot.goto((0,0,0))
