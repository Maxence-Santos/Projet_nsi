import rsk
from os import system
from metrics import *
from math import pi

def print_the_ball(client, dt):
    print(client.ball)


def attaque(cote, robot):
    SIDE = cote # je sais que c'est pas bien mais flemme de tout changer et en plus ca se voit mieux
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
        while client.ball is None:
            print("Waiting to detect the ball...")
            system("cls") # ou clear
        pos_bal = client.ball
        need_update = False
        angle_a = None
        
        while True:
            print("555")
            try :
                
                if client.ball is not None and pos_bal[0] != client.ball[0] and pos_bal[1] != client.ball[1]:
                    pos_bal = client.ball
                    need_update = True
                
                them_pos = [client.robots[them][1].pose,
                        client.robots[them][2].pose]
                us_pos = [client.robots[us][1].pose,
                        client.robots[us][2].pose]
                dist = get_distance(pos_bal, robot)
                needed_distance = 0.091
                
                
                # Déplacement attaquant
                if (robot.pose[0] + (needed_distance - 0.05) > pos_bal[0] and SIDE == "d") or \
                (robot.pose[0] + (needed_distance - 0.05) < pos_bal[0] and SIDE == "g"):
                    robot.goto((pos_bal[0] + diff_dist ,robot.pose[1], default ))
                    robot.goto((robot.pose[0],pos_bal[1], default ))
                else:
                    
                    if angle_a is None or need_update:
                        angle_a = get_angle_att(pos_bal, SIDE, them_pos, robot.pose)
                        pos_att = get_pos_cadre(pos_bal, SIDE, angle_a)
                        need_update = False
                    robot.goto((pos_att[0],pos_att[1], angle_a ), wait=False)
                
                
                if dist < 0.091:
                    robot.kick()
                

            except rsk.client.ClientError as e:
                print(e)
        
if __name__=="__main__":
    with rsk.Client(host='172.19.66.163', key='',wait_ready=False) as client:
        robotBleu1 = client.robots['blue'][1]
        attaque("d", robotBleu1)