# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:36:40 2026

@author: celian.mludek
"""
from time import*

def lecture_fichier(nom):
    contenu =""
    with open(nom, 'r', encoding="utf8") as fichier:
        contenu = fichier.read() 
    return contenu


def recherche(motif, texte):
    liste = []
    for i in range(len(texte)):
        j = 0
        while j < len(motif) and texte[i+j] == motif[j]:
            j =  j + 1
        if j == len(motif):
            liste.append(i)
    return liste
            

def temps_execution(fonction, motif, texte):
    debut = time()
    fonction(motif, texte)
    fin = time()
    return fin - debut


def tests():
    assert lecture_fichier("test.txt") == "abcdefghijklmnopqrstuvwxyz", "la fonction lecture_fichier ne fonctionne pas"
    texte = lecture_fichier("test.txt")
    assert recherche("abcdefg", texte) == [0], "la fonction recherche(motif, texte) ne fonctionne passsss"
    assert recherche("abcdefgportfaux", texte) == [], "la fonction recherche(motif, texte) ne fonctionne pas"
    
    
if __name__ == "__main__":
    # je lance les tests
    tests()
    print("tests vaildés")
