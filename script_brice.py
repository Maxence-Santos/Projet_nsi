import rsk
from os import system
from metrics import *
import numpy as np
from math import pi
from time import sleep


def print_the_ball(client, dt):
    print(client.ball)

SIDE = "d"


if SIDE == "d":
    us = "blue"
    them = "green"
    default = 0
    diff_dist = - 0.2
else:
    us = "green"
    them = "blue"
    default = pi
    diff_dist =  0.2

with rsk.Client(host='172.19.66.163', key='',wait_ready=False) as client: # ou 228
    # Connection
    robotBleu2 = client. robots[us][2]
    robot1 = client. robots[us][1]
    while client.ball is None:
        print("Waiting to detect the ball...")
        system("cls") # ou clear
    pos_bal = client.ball
    need_update = False
    angle_a = None
    
    while True:
        
        if client.ball is not None and pos_bal[0] != client.ball[0] and pos_bal[1] != client.ball[1]:
            pos_bal = client.ball
            need_update = True
          
        them_pos = [client.robots[them][1].pose,
                client.robots[them][2].pose]
        us_pos = [client.robots[us][1].pose,
                client.robots[us][2].pose]
        needed_distance = estimate_distance(pos_bal)
        dist = get_distance(pos_bal, robot1)
        
        
        # Déplacement attaquant
        if (robot1.pose[0] + (needed_distance - 0.05) > pos_bal[0] and SIDE == "d") or \
        (robot1.pose[0] + (needed_distance - 0.05) < pos_bal[0] and SIDE == "g"):
            robot1.goto((pos_bal[0] + diff_dist ,robot1.pose[1], default ))
            robot1.goto((robot1.pose[0],pos_bal[1], default ))
        else:
            
            if angle_a is None or need_update:
                angle_a = get_angle_att(pos_bal, SIDE, them_pos, robot1.pose)
                pos_att = get_pos_cadre(pos_bal, SIDE, angle_a)
                need_update = False
            robot1.goto((pos_att[0],pos_att[1], angle_a ), wait=False)
        

        if abs(pos_bal[0] - robot1.pose[0]) < 0.09:
            robot1.kick()
        
        print(f"Distance : {dist:.3f}")
        print(f"Prédit : {needed_distance:.3f}")
        
        print(f"X1 : {pos_bal[0]:.3f}, X2 : {pos_bal[1]:.3f}, X3 : {robot1.pose[2]:.3f}, Y : {dist:.3f}")
        sleep(0.05)
        
        
