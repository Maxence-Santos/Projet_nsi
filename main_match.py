import rsk
import Goal
from attaque import attaque
from os import system
from threading import Thread

SIDE = "g"


if SIDE == "d":
    cote = 1
    OPPOSITE = "g"
    pas_cote = 0
else:
    cote = 0
    OPPOSITE = "d"
    pas_cote = 1


with rsk.Client(host='172.19.66.163', key='') as client:
    robotVert1 = client.robots['green'][1]
    robotVert2 = client.robots['green'][2]
    robotBleu1 = client.robots['blue'][1]
    robotBleu2 = client.robots['blue'][2]

    

    while client.ball is None:
        print("Waiting to detect the ball...")
        system("cls") # ou clear
    pos_balle = client.ball


    thread_goal_vert = Thread(target=Goal.goal, args=(robotVert2,SIDE))
    thread_attaque_vert = Thread(target=attaque, args=(SIDE, robotVert1))
    thread_goal_bleu = Thread(target=Goal.goal, args=(robotBleu2,OPPOSITE))
    thread_attaque_bleu = Thread(target=attaque, args=(OPPOSITE, robotBleu1))



    threads = []
    for t in [thread_goal_vert, thread_attaque_vert, thread_goal_bleu,thread_attaque_bleu]:
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        