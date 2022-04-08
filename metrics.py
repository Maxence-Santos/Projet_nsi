from math import atan, pi, sqrt, cos, sin
from random import choice
from numpy import linspace

goal_droit= [ # coté vert (c1 et c2)
  (0.9, 0.3), # poteaux supérieur, (x,y)
  (0.9,-0.3)  ] # poteaux inférieur, (x,y)
goal_gauche= [
  (-0.9, 0.3),
  (-0.9, -0.3)  ]

terrain_x = [-0.9, 0.9]
terrain_y = [-0.6, 0.6]

distance_kick = 0.11

def get_alpha(pos_balle:tuple, goal:list):
  """
  Retourne les deux angles alpha (voir les explications) qui serviront pour le calcul de theta.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - goal: list - contient les coordonnées des poteaux du goal 
  """
  up_1 = (pos_balle[1]-goal[0][1])**2
  up_2 = (pos_balle[1]-goal[1][1])**2
  down = (pos_balle[0]-goal[0][0])**2
  return (atan ( sqrt( up_1 / down ) ), 
        atan ( sqrt( up_2 / down ) ))
  
def get_theta_att(pos_balle:tuple, cote:str):
  """
  Retourne les deux angles theta (voir les explications) pour que l'attaquant puisse cadrer.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - cote : str - Côté que l'on attaque. d pour droite, g pour gauche 
                    ( par rapport au sens de l'axe des abscisses ) 
    
  """
  if cote.lower() == "d":
    alpha = get_alpha(pos_balle, goal_droit)
    if pos_balle[1] > 0:
      return ( - alpha[0],
             - alpha[1])
    else:
      return (alpha[0],
              alpha[1])
  elif cote.lower() == "g":
    alpha = get_alpha(pos_balle, goal_gauche)
    if pos_balle[1] > 0:
      return ( alpha[0] - pi,
               alpha[1] - pi)
    else:
      return (pi - alpha[0],
              pi - alpha[1])

def get_theta_vers_goal(pos_balle:tuple,cote:str, joueurs:list):
  """
  A faire
  """
  if cote.lower() == "d":
    if joueurs[0][0] >  joueurs[1][0]:
      joueur = joueurs[0]
    else:
      joueur = joueurs[1]
  if cote.lower() == "g":
    if joueurs[0][0] <  joueurs[1][0]:
      joueur = joueurs[0]
    else:
      joueur = joueurs[1]
  up = (pos_balle[1]-joueur[1])**2
  down = (pos_balle[0]-joueur[0])**2
  alpha = atan ( sqrt( up / down ) )
  if cote.lower() == "d":
    if pos_balle[1] > 0:
      return - alpha, joueur
    else:
      return  alpha , joueur
  elif cote.lower() == "g":
    if pos_balle[1] > 0:
      return alpha - pi, joueur
    else:
      return pi - alpha, joueur
    
def get_theta_def(pos_balle:tuple, cote:str):
  """
  Retourne les deux angles theta (voir les explications) pour que le goal soit aligné avec la balle.
  Ceux-ci sont calculés en fonction des deux poteaux pour avoir les deux "extrémités" pour être correctement alignées.
  
  Paramètres:
    - pos_balle : tuple - contient les positions x et y de la balle
    - cote : str - Côté que l'on attaque. d pour droite, g pour gauche 
                    ( par rapport au sens de l'axe des abscisses ) 
  """
  if cote.lower() == "d":
    alpha = get_alpha(pos_balle, goal_droit)
    if pos_balle[1] > 0:
      return (pi - alpha[0],
              pi - alpha[1])
    else:
      return (pi + alpha[0],
              pi/2 + alpha[1])
  elif cote.lower() == "g":
    alpha = get_alpha(pos_balle, goal_gauche)
    if pos_balle[1] > 0:
      return (alpha[0],
              alpha[1])
    else:
      return (-alpha[0],
              -alpha[1])

def get_theta_goal(pos_att:tuple,cote_attaque:str, joueur:list):
  if cote_attaque.lower() == "d":
    alpha = [get_alpha(pos_att, [goal_droit[0], tuple(joueur)]),
              get_alpha(pos_att, [goal_droit[1], tuple(joueur)])
              ]
    if pos_att[1] > 0:
      angles =[ (- alpha[0][0],
             - alpha[0][1]),
             (- alpha[1][0],
             - alpha[1][1])]
    else:
      angles = [ (alpha[0][0],
               alpha[0][1]), 
              (alpha[1][0],
              alpha[1][1])]
  elif cote_attaque.lower() == "g":
    alpha = [get_alpha(pos_att, [goal_gauche[0], tuple(joueur)]),
              get_alpha(pos_att, [goal_gauche[1], tuple(joueur)])]
    if pos_att[1] > 0:
      angles = [ ( alpha[0][0] - pi,
              alpha[0][1] - pi),
              (alpha[1][0] - pi,
              alpha[1][1] - pi)]
    else:
      angles = [(pi - alpha[0][0],
              pi - alpha[0][1]),
              (pi - alpha[1][0],
              pi - alpha[1][1])]

def get_angle_att(pos_balle:tuple, cote_attaque:str, joueurs:list, pos_att:list):
  """Retourne l'angle que doit avoir l'attaquant

  Args:
      pos_balle (tuple)
      cote_attaque (str): d ou g

  Returns:
      float
  """
  theta = get_theta_att(pos_balle, cote_attaque)
  theta_adv, joueur = get_theta_vers_goal(pos_balle, cote_attaque, joueurs)
  print(theta, theta_adv)
  if min(theta) < theta_adv < max(theta):
    alpha = None
    if cote_attaque.lower() == "d" and joueur[0] > pos_balle[0] or cote_attaque.lower() == "g" and joueur[0] < pos_balle[0]:
      thetas = get_theta_goal(pos_balle, cote_attaque, joueur)
      
  angle_values = linspace(min(theta),max(theta),100)[25:75]
  return choice(angle_values)

def get_pos_cadre(pos_balle:tuple, cote_attaque:str, angle:float):
  """Permet de pouvoir récupérer la position que doit avoir le joueur, en se décalant un peu de la balle pour ne pas lui rouler dessus 

  Args:
      pos_balle:tuple: Contient client.ball, la position de la balle

  Returns:
      (x,y)  tuple: Position vers laquelle le joueur doit aller
  """
  x_balle = pos_balle[0]
  y_balle = pos_balle[1]

  theta = angle # juste pour la lisibilité
  x_hat = abs(0.09 * cos(theta))
  y_hat = abs(0.09 * sin(theta))

  #Cas x- et y-
  if x_balle < 0 and y_balle < 0:
    x = x_balle + x_hat
    y = y_balle - y_hat
  
  #Cas x- et y+
  if x_balle < 0 and y_balle > 0:
    x = x_balle + x_hat
    y = y_balle + y_hat
  
  #cas x+ et y+
  if x_balle > 0 and y_balle > 0:
    x = x_balle - x_hat
    y = y_balle + y_hat
  
  #Cas x+ et y-
  if x_balle > 0 and y_balle < 0:
    x = x_balle - x_hat
    y = y_balle - y_hat
      
  return (x,y)


def get_angle_def(pos_balle:tuple, cote_attaque:str):
  """Retourne l'angle que doit avoir le  goal

  Args:
      pos_balle (tuple)
      cote_attaque (str): d ou g

  Returns:
      float
  """
  return sum(list(get_theta_def(pos_balle, cote_attaque))) / 2

def get_distance(pos_element:tuple,joueur):
  """Est-ce que je dois vraiment faire une doc?"""
  pos_joueur = joueur.pose
  return sqrt((pos_element[0] - pos_joueur[0])**2 + 
        (pos_element[1] - pos_joueur[1])**2)



if __name__=="__main__":
    pass
