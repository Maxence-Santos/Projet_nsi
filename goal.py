import rsk
from metrics import *

zone_goal_gauche= [ # coté vert (c1 et c2)
  (-0.6, 0.45), # poteaux supérieur, (x,y)
  (-0.6,-0.45)  ] # poteaux inférieur, (x,y)
zone_goal_droit= [
  (0.6, 0.45),
  (0.6, -0.45)  ]  


def goal(pos_balle,pos_robot,robot):
    if pos_balle[0] + pos_robot[0] < 0.05:
        robot.kick()
    if pos_balle[0] >= 0.85:
        x = -0.75
        y = pos_balle[1] /2
    else:
        x = -0.7
        y = pos_balle[1]
    return (x,y)
