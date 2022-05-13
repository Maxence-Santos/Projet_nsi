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
  angles = []
  if cote.lower() == "d":
    alphas = get_alpha(pos_balle, goal_droit)
    for alpha, poteau in zip(alphas, goal_droit):
      if pos_balle[1] > poteau[1]:
        angles.append(-alpha)
      else:
        angles.append(alpha)
  elif cote.lower() == "g":
    alphas = get_alpha(pos_balle, goal_gauche)
    for alpha, poteau in zip(alphas, goal_gauche):
      if pos_balle[1] > poteau[1]:
        angles.append(alpha + pi)
      else:
        angles.append(pi - alpha)
  return angles

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
    if pos_balle[1] > joueur[1]:
      return - alpha, joueur
    else:
      return  alpha , joueur
  elif cote.lower() == "g":
    if pos_balle[1] > joueur[1]:
      return alpha + pi, joueur
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
  angles = []
  if cote.lower() == "d":
    alphas = get_alpha(pos_balle, goal_droit)
    for alpha, poteau in zip(alphas, goal_droit):
      if pos_balle[1] > poteau[1]:
        angles.append(alpha)
      else:
        angles.append(-alpha)
  elif cote.lower() == "g":
    alphas = get_alpha(pos_balle, goal_gauche)
    for alpha, poteau in zip(alphas, goal_gauche):
      if pos_balle[1] > poteau[1]:
        angles.append(pi - alpha)
      else:
        angles.append(alpha - pi)
  return angles


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
  if min(theta) < theta_adv < max(theta):
    if cote_attaque.lower() == "d" and joueur[0] > pos_balle[0] or cote_attaque.lower() == "g" and joueur[0] < pos_balle[0]:
      thetas = [(theta[0], theta_adv), (theta[1], theta_adv)]
      if abs(thetas[0][0] - thetas[0][1]) > abs(thetas[1][0] - thetas[1][1]):
        theta = thetas[0]
      else:
        theta = thetas[1]

  print(theta)
  return sum(list(theta)) / 2

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
  x_hat = abs(0.08 * cos(theta))
  y_hat = abs(0.08 * sin(theta))


  if cote_attaque.lower() == "g":
    if y_balle < 0:
      x = x_balle + x_hat
      y = y_balle - y_hat
    else:
      x = x_balle + x_hat
      y = y_balle + y_hat
  elif cote_attaque.lower() == "d":
    if y_balle > 0:
      x = x_balle - x_hat
      y = y_balle + y_hat
    else:
      x = x_balle - x_hat
      y = y_balle - y_hat
      
  return (x,y)


def get_angle_def(pos_balle:tuple, cote_attaquant:str):
  """Retourne l'angle que doit avoir le  goal

  Args:
      pos_balle (tuple)
      cote_attaquant (str): d ou g

  Returns:
      float
  """
  return sum(list(get_theta_att(pos_balle, cote_attaquant))) / 2 + pi


def get_distance(pos_element:tuple,joueur):
  """Est-ce que je dois vraiment faire une doc?"""
  pos_joueur = joueur.pose
  return sqrt((pos_element[0] - pos_joueur[0])**2 + 
        (pos_element[1] - pos_joueur[1])**2)

def estimate_distance(pos_balle):
  x_balle = pos_balle[0]
  return -0.02 * x_balle + 0.11 # trouvé par regression linéaire

def estimate_distance2(pos_balle, joueur):
  x_balle = pos_balle[0]
  y_balle = pos_balle[1]
  x_balle -= (x_balle * 0.042) / 2.6
  y_balle -= (y_balle * 0.042) / 2.6
  return get_distance((x_balle,y_balle),
  joueur) # merci gregwar, en fait non

def estimate_distance3(pos_balle):
  x_balle = pos_balle[0]
  return -0.006 * x_balle + 0.099 # trouvé par regression linéaire

if __name__=="__main__":
    pass
