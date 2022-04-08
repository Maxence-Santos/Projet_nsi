import rsk
from math import pi, sqrt,radians
from metrics import *

zone_goal_gauche= [ # coté vert (c1 et c2)
  (-0.6, 0.45), # poteaux supérieur, (x,y)
  (-0.6,-0.45)  ] # poteaux inférieur, (x,y)
zone_goal_droit= [
  (0.6, 0.45),
  (0.6, -0.45)  ]  

d = False

def goal(pos_balle,robot):
    pos_robot = robot.position
    print(pos_robot[0] - pos_balle[0])
    if d:
        #distance = sqrt((pos_balle[0] - pos_robot[0])**2 + (pos_balle[1] - pos_robot[1]) **2)
        if abs(pos_robot[0] - pos_balle[0]) < 0.12: #distance < 0.11:
            robot.kick()
        a = sum(list(get_theta_def(pos_balle,"g"))) / 2
        if pos_balle[0] <= 0.6 :
            x = 0.8
            y = pos_balle[1] /2
        else:
            x = pos_balle[0]
            y = pos_balle[1]
    else:
        """distance = sqrt((pos_balle[0] - pos_robot[0])**2 + 
            (pos_balle[1] - pos_robot[1])**2)
        if distance < 0.05:
            robot.kick()"""
        #distance = sqrt((pos_balle[0] - pos_robot[0])**2 + (pos_balle[1] - pos_robot[1]) **2)
        if abs(pos_robot[0] - pos_balle[0]) < 0.12: #distance < 0.11:
            robot.kick()
        a = sum(list(get_theta_def(pos_balle,"d"))) / 2
        if pos_balle[0] >= -0.6 :
            x = -0.8
            y = pos_balle[1] /2
        else:
            x = -0.7
            y = pos_balle[1]
    robot.goto((x,y,a), wait=False)
