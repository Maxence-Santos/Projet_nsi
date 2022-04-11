import rsk
from os import system
from metrics import *
from goal import *
import numpy as np
from math import pi

rsk.robot.Robot("/dev/rfcomm0")

def print_the_ball(client, dt):
    print(client.ball)

with rsk.Client(host='172.19.66.163', key='') as client:
    robotBleu2 = client. robots['blue'][2]
    robotBleu1 = client. robots['blue'][1]
    pos_bal = client.ball
    need_update = False
    angle_a = None
    while True:
        """
        if pos_bal[0] != client.ball[0] and pos_bal[1] != client.ball[1]:
            pos_bal = client.ball
            need_update = True
            
        verts = [client.robots['green'][1].pose,
                client.robots['green'][2].pose]
        bleus = [client.robots['blue'][1].pose,
                client.robots['blue'][2].pose]
        needed_distance = estimate_distance(pos_bal)
        dist = get_distance(pos_bal, robotBleu1)
        
        if robotBleu1.pose[0] + (needed_distance - 0.05) > pos_bal[0]:
            robotBleu1.goto((pos_bal[0] - 0.2 ,robotBleu1.pose[1], 0 ))
            robotBleu1.goto((robotBleu1.pose[0],pos_bal[1], 0 ))
        else:
            
            if angle_a is None or need_update:
                angle_a = get_angle_att(pos_bal, "d", verts, robotBleu1.pose)
                pos_att = get_pos_cadre(pos_bal, "d", angle_a)
                need_update = False
            #robotBleu1.goto((pos_att[0],pos_att[1], angle_a ), wait=False)

        if dist < needed_distance  :
            robotBleu1.kick()
            """
        client.blue1.leds(255,255,255)
        print(f"Distance : {dist:.3f}, estimation : {needed_distance:.2f}")
        
