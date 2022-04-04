import rsk
from os import system
from metrics import *
from goal import *

def print_the_ball(client, dt):
    print(client.ball)

with rsk.Client(host='172.19.66.163', key='') as client:
    robotBleu2 = client. robots['blue'][2]
    robotVert1 = client. robots['green'][1]
    while True:
        """
        for i, robot in enumerate(robots):
            pos = robot.position
            print(f"Robot {i} : x={pos[0]}   y={pos[1]}")
        ball_pos = client.ball
        print(client.robots['green'][1].pose)
        client.on_update = print_the_ball
        """
        angle_d = get_angle_def(pos_bal, "g")
        pos_bal = client.ball
        pos_goal = goal(pos_bal)
        robotBleu2.goto((pos_goal[0],pos_goal[1], angle_d), wait=False)

        if get_distance_balle(pos_bal, robotBleu2) < 0.05:
            robotBleu2.kick()
        
        angle_a = get_angle_att(pos_bal, "g")
        pos_att = get_pos_cadre(pos_bal)
        robotVert1.goto((pos_att[0],pos_att[1], angle_a), wait=False)
        if get_distance_balle(pos_bal, robotVert1) < 0.05:
            robotVert1.kick()
