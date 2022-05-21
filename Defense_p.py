import rsk
from metrics import *

def pos_def(pos_balle,pos_robot_adv,robot,cote):
    try:
        pos_robot = robot.position

        if abs(pos_robot_adv[0] - pos_balle[0]) < 0.15:
            a = sum(list(get_theta_def(pos_balle, cote))) / 2
            if cote != "g":
                if pos_balle[1] >= 0 and pos_balle[0] < 0:
                    robot.goto((pos_balle[0] + 0.2,pos_balle[1] - 0.1,a))
                elif pos_balle[1] < 0 and pos_balle[0] < 0:
                    robot.goto((pos_balle[0] + 0.2,pos_balle[1] + 0.1,a)) 
            else:
                if pos_balle[1] >= 0 and pos_balle[0] >= 0:
                    robot.goto((pos_balle[0] - 0.2,pos_balle[1] - 0.1,a))
                elif pos_balle[1] < 0 and pos_balle[0] >= 0:
                    robot.goto((pos_balle[0] - 0.2,pos_balle[1] + 0.1,a))
        
        else:
            robot.goto((0,0,0), wait=False)

    except rsk.client.ClientError as e:
        print(e)