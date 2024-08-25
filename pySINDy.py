class vehicule:
  """
  Voici un exemple de classe "vehicule" qui contient le plan de conception
  d'objets "véhicules"
  """

  # Une classe commence par une fonction initialisation qui contient les différents attributs
  def __init__(self, couleur='noire', vitesse=0, roues=4):
    self.couleur = couleur
    self.vitesse = vitesse
    self.roues = roues
    
  # voici une méthode "accelerer" qui modifie un attribut de l'objet
  def accelerer(self, vitesse):
    self.vitesse += vitesse

  # voici une autre méthode
  def stop(self):
    self.vitesse = 0

  # voici une derniere méthode, tres souvent utilisée
  def afficher(self):
    print(f'couleur: {self.couleur}\nroues: {self.roues}\nvitesse: {self.vitesse}')

# création d'un objet de la classe voiture
voiture_1 = vehicule(couleur='rouge')
     

voiture_1.accelerer(100)
     

voiture_1.afficher()