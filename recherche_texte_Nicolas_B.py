# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def ouvrir(nom_fichier):
    contenu =""
    with open(nom_fichier, 'r', encoding="utf8") as fichier:
        contenu = fichier.read() 
    return contenu

def occurence(chaine,motif):
    liste=[]
    i=0
    j=0
    while i != len(chaine):
        
        if chaine[i]==motif[j]:
            j+=1
        else:
            j=0
        if j == len(motif):
            liste.append(i-j)
            j=0
        i+=1
    return liste





chaine = ouvrir("Vingt mille lieues sous les mers.txt")
print(occurence(chaine,"bonjour"))

chaine = ouvrir("Secret.txt")
print(occurence(chaine,"le"))
            
            
