import rsk
from os import system
from metrics import *
from goal import *

def print_the_ball(client, dt):
    print(client.ball)

with rsk.Client(host='172.19.66.163', key='') as client:
    robotBleu2 = client. robots['blue'][2]
    robotBleu1 = client. robots['blue'][1]
    while True:
        pos_bal = client.ball
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

            """
        angle_a = get_theta_att(pos_bal, "d")
        angle_a = get_angle_att(pos_bal, "d")
        print(angle_a)
        pos_att = get_pos_cadre(pos_bal, "d")
        robotBleu1.goto((pos_att[0],pos_att[1], angle_a ), wait=False)
        # robotBleu1.goto((robotBleu1.pose[0],robotBleu1.pose[1], -0.6), wait=False)

        dist = get_distance(pos_bal, robotBleu1)
        print(dist)
        
        if  dist < 0.11:
            robotBleu1.kick()
