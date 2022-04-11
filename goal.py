import rsk
from math import pi, sqrt,radians
from metrics import *
import metrics_test

zone_goal_gauche= [ # coté vert (c1 et c2)
  (-0.6, 0.45), # poteaux supérieur, (x,y)
  (-0.6,-0.45)  ] # poteaux inférieur, (x,y)
zone_goal_droit= [
  (0.6, 0.45),
  (0.6, -0.45)  ]  

d = True

def goal(pos_balle,robot):
    pos_robot = robot.position
    print(pos_robot[0] - pos_balle[0])
    if d:
        if abs(pos_robot[0] - pos_balle[0]) < 0.12:
            robot.kick()
        a = metrics_test.get_angle_def(pos_balle, "g")
        if pos_balle[0] <= 0.6 :
            x = 0.8
            y = pos_balle[1] /2
        else:
            x = pos_balle[0]
            y = pos_balle[1]
    else:
        if abs(pos_robot[0] - pos_balle[0]) < 0.12:
            robot.kick()
        a = metrics_test.get_angle_def(pos_balle, "d")
        if pos_balle[0] >= -0.6 :
            x = -0.8
            y = pos_balle[1] /2
        else:
            x = -0.7
            y = pos_balle[1]
    robot.goto((x,y,a), wait=False)
    print("yo")
