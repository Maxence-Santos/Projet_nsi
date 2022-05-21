import rsk
from metrics import *

def goal(robot,cote):
    with rsk.Client(host='172.19.66.163', key='') as client:

        while True:
            try :
                pos_robot = robot.position
                if client.ball is not None:
                    pos_balle = client.ball
                # print(pos_robot[0] - pos_balle[0])
                if cote != "d":
                    if abs(pos_robot[0] - pos_balle[0]) < 0.15:
                        robot.kick()
                    a = get_angle_def(pos_balle, "d")
                    if pos_balle[0] <= 0.4 :
                        x = 0.8
                        y = pos_balle[1] /2 # tester par rapport aux poteaux
                    else:
                        x = pos_balle[0]
                        y = pos_balle[1]
                else:
                    if abs(pos_robot[0] - pos_balle[0]) < 0.15:
                        robot.kick()
                    a = get_angle_def(pos_balle, "g")
                    if pos_balle[0] >= -0.4 :
                        x = -0.8
                        y = pos_balle[1] /2
                    else:
                        x = pos_balle[0]
                        y = pos_balle[1]
                robot.goto((x,y,a), wait=False)
            except rsk.client.ClientError as e:
                print(e)