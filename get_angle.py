# N'a pas été testé
from math import atan, pi, sqrt,


goal_droit= [
  (0, 0),
  (0,0)  ]
goal_gauche= [
  (0, 0),
  (0,0)  ]

terrain_x = [-0.9, 0.9]

def get_alpha(pos_joueur:tuple, goal:list):
  """
  Retourne l'angle alpha (voir les explications) qui serviront pour le calcul de theta
  
  Paramètres:
    - pos_joueur : tuple - contient les positions x et y du joueur
  """
  up = (goal[0][0]-pos_joueur[0])**2
  down_1 = (pos_joueur[1]-goal[0][1])**2
  down_2 = (pos_joueur[1]-goal[1][1])**2
  return atan ( sqrt( up / down_1 ) ), 
         atan ( sqrt( up / down_2 ) )
  
def get_theta():
  pass
