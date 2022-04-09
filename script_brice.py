import rsk
from os import system
from metrics import *
from goal import *
import numpy as np
import metrics_test
from math import copysign, pi

def print_the_ball(client, dt):
    print(client.ball)

with rsk.Client(host='172.19.66.163', key='') as client:
    robotBleu2 = client. robots['blue'][2]
    robotBleu1 = client. robots['green'][1]
    pos_bal = client.ball
    need_update = False
    angle_a = None
    while True:
        if pos_bal[0] != client.ball[0] and pos_bal[1] != client.ball[1]:
            pos_bal = client.ball
            need_update = True
        verts = [client.robots['green'][1].pose,
                client.robots['green'][2].pose]
        bleus = [client.robots['blue'][1].pose,
                client.robots['blue'][2].pose]
        print(get_distance(pos_bal, robotBleu1))
        """
        for i, robot in enumerate(robots):
            pos = robot.position
            print(f"Robot {i} : x={pos[0]}   y={pos[1]}")
        ball_pos = client.ball
        print(client.robots['green'][1].pose)
        client.on_update = print_the_ball
        

        angle_d = get_angle_def(pos_bal, "g")
        
        pos_goal = goal(pos_bal)
        robotBleu2.goto((pos_goal[0],pos_goal[1], angle_d), wait=False)

        if get_distance_balle(pos_bal, robotBleu2) < 0.05:
            robotBleu2.kick()

            
        if verts[0][0] - 0.09 < pos_bal[0]:
            robotBleu1.goto((pos_bal[0] + 0.2 ,robotBleu1.pose[1], pi ))
            robotBleu1.goto((robotBleu1.pose[0],pos_bal[1], pi ))
        else:
            
            if angle_a is None or need_update:
                angle_a = metrics_test.get_angle_att(pos_bal, "g", bleus, robotBleu1.pose)
                pos_att = metrics_test.get_pos_cadre(pos_bal, "g", angle_a)
                need_update = False
            # robotBleu1.goto((pos_att[0],pos_att[1], angle_a ), wait=False)
            # robotBleu1.goto((robotBleu1.pose[0],robotBleu1.pose[1], -0.6), wait=False)
            
            dist = get_distance(pos_bal, robotBleu1)
            print(dist)
            if dist < 0.0001:
                robotBleu1.kick()
"""
