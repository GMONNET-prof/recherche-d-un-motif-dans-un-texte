# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:02:36 2026

@author: mathis.bruc
"""

from time import * 

def ouvrir(nom_fichier):
    contenu =""
    with open(nom_fichier, 'r', encoding="utf8") as fichier:
        contenu = fichier.read() 
    return contenu

def recherche(motif,texte):
    liste = []
    for i in range(len(texte)) :
        j = 0
        while j < len(motif) and motif[j] == texte[i+j]:
            
            j += 1
        if j == len(motif):
            liste.append(i)
    return liste

texte = ouvrir("texte.txt")
print(recherche("ma",texte))