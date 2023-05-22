#!/usr/bin/python3
# -*-coding:utf-8-*-
# Importation du module math
from math import *

"""Crée une classe Cercle en python, dotée d'un attribut rayon,
d'une méthode perimetre() pou calculer le périmètre du cercle
 et une méthode surface() pour calculer la surface du cercle.
 Crée également une classe fille Cylindre héritant de la classe Cercle
 , dotée d'un attribut hauteur et une méthode volume()
 pour calculer le volume du cylindre."""

# Creation de la classe Cercle
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    # Méthode calculant le périmètre
    def perimetre(self):
        return 2 * pi * self.rayon

    # Méthode calculant la surface
    def surface(self):
        return pi * (self.rayon ** 2)

#Création de la classe fille Cylindre
class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur

    # Méthode calculant le voloume
    def volume(self):
        return (self.rayon ** 2) * pi * self.hauteur

# Créer un objet cercle et cylindre
mon_cercle = Cercle(4)
mon_cylindre = Cylindre(4, 8)

#À partir de ces objets calculons et affichons le périmètre
# et la surface du cercle. Puis le volume du cylindre
print("Le périmètre de mon cercle est : ", mon_cercle.perimetre())
print("La surface de mon cercle est : ", mon_cercle.surface())
print("Le volume de mon cylindre est : ", mon_cylindre.volume())
