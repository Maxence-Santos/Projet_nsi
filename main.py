import rsk
#import metrics
import Goal
from math import pi, sqrt
import Defense

with rsk.Client(host='172.19.66.163', key='') as client:
    robotVert1 = client.robots['green'][1]
    robotVert2 = client.robots['green'][2]
    robotBleu1 = client.robots['blue'][1]
    robotBleu2 = client.robots['blue'][2]

    while True:
        pos_balle = client.blue1.pose # client.ball
        pos_robot_adv = robotBleu1.position
        Goal.goal(pos_balle,robotVert2)
        #Defense.pos_def(pos_balle,pos_robot_adv,robotVert1)
