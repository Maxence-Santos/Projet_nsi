import rsk
from os import system
from get_angle import *
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
        angle_d = sum(list(get_theta_def(client.ball, "d"))) / 2
        pos_bal = client.ball
        pos_goal = goal(pos_bal)
        robotBleu2.goto((pos_goal[0],pos_goal[1], angle_d), wait=False)

        if sqrt((pos_goal[0] - robotBleu2.pose[0])**2 + # a changer
        (pos_goal[1] - robotBleu2.pose[1])**2) < 0.055:
            robotBleu2.kick()
        
        angle_a = sum(list(get_theta_att(client.ball, "g"))) / 2
        pos_att = get_pos(pos_bal)
        robotVert1.goto((pos_att[0],pos_att[1], angle_a), wait=False)
        if sqrt((pos_att[0] - robotVert1.pose[0])**2 + 
        (pos_att[1] - robotVert1.pose[1])**2) < 0.055:
            robotVert1.kick()
