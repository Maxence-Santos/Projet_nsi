import rsk
from math import pi, sqrt,radians
from metrics import *
from attaque import attaque

def pos_def(robot_adv,goal,robot,cote):
    with rsk.Client(host='172.19.66.163', key='') as client:
        while True:
            try:
                if client.ball is not None:
                        pos_balle = client.ball
                pos_robot_adv = robot_adv.pose
                pos_goal = goal.pose
            
                pos_robot_x = (pos_balle[0] + pos_goal[0]) /2
                pos_robot_y = (pos_balle[1] + pos_goal[1]) /2
                if abs(pos_robot_adv[0] - pos_balle[0]) < 0.15 and abs(pos_robot_adv[1] - pos_balle[1] < 0.1):
                    if not cote and pos_balle[1] >= 0 and pos_balle[0] < 0:
                        a = sum(list(get_theta_def(pos_balle,"g"))) / 2
                        robot.goto((pos_robot_x + 0.2,pos_robot_y - 0.1,a))
                    elif not cote and pos_balle[1] < 0 and pos_balle[0] < 0:
                        a = sum(list(get_theta_def(pos_balle,"g"))) / 2
                        robot.goto((pos_robot_x + 0.2,pos_robot_y + 0.1,a))
                    
                    else:
                        if cote and pos_balle[1] >= 0 and pos_balle[0] >= 0:
                            a = sum(list(get_theta_def(pos_balle,"d"))) / 2
                            robot.goto((pos_robot_x - 0.2,pos_robot_y - 0.1,a))
                        elif cote and pos_balle[1] < 0 and pos_balle[0] >= 0:
                            a = sum(list(get_theta_def(pos_balle,"d"))) / 2
                            robot.goto((pos_robot_x - 0.2,pos_robot_y + 0.1,a))
                
                else:
                    if abs(pos_balle[0] - robot.pose[0]) <= 0.3 and abs(pos_balle[1] - robot.pose[1]) <= 0.15:
                        attaque(cote,robot)
                    else:
                        robot.goto((0,0,0))
            except rsk.client.ClientError as e:
                print(e)