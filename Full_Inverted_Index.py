# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:52:37 2021

@author: fonsi
"""

import re
import numpy as np

#Vector que combina en uno solo todas las caraterísticas de cada palabra (ver linea 87)

#Array who merges all the features of each word (View Line 86)

def vectorfii(doc,rep,pos):
    dato=[]
    dato.append(doc)
    dato.append(rep)
    pos = pos.astype('int')
    dato.append(pos)
    total = []
    total.append(dato)
    return total
    

#Documentos de prueba ingresados en un vector (Test Documents)

coleccion1 = ["To do is to be. To be is to do.",
"To be or not to be I am what I am.",
"I think therefore I am. Do be do be do.",
"Do do do, da da da. Let it be, let it be"]

listaM = []
#Transformación a Minúsculas(Change to Lower Case)
for n in coleccion1:
    listaM.append(n.lower())

listaS = []
#Eliminacion de Caracteres Especiales (Delete Special Characters)
for n in listaM:
    listaS.append(re.sub('[,.()"-]', '',n))



union = " ".join(listaS)
print("**UNION**")
print(union)

# tokenizacion
diccionario = set(union.split())
listaD = list(diccionario)
print("**DICCIONARIO**")
print(listaD)
print("El tamaño del diccionario es:",len(listaD))




def full_inverted_index(diccionario,coleccion):
    posiciones = []
    for n in range(0,len(diccionario)):
        cont = 0
        for m in range(0,len(coleccion)):
            x = coleccion[m].split()
            array = np.array(x)
            if(diccionario[n] in x):
                rep = x.count(diccionario[n])
                pos = np.where(array ==diccionario[n])[0]        
                dato = vectorfii(m, rep, pos)
                cont+=1
            if(cont==1):
                dato.insert(0, diccionario[n])
                posiciones.append(dato)
            else:
                posiciones[-1].append(dato)    
    return posiciones



                
respuesta = full_inverted_index(listaD, listaS)


print("===Full inverted Index===")
print("En el orden de las palabras en el diccionario")
#Return array with: (Word, Document, Frecuency of the word, Positions of the word in the document)
print("Palabra,Documento,Nro de Repeticiones,[posiciones en el documento]") 

for i in range(len(respuesta)):
    print(respuesta[i])               
            
#print(posiciones)            
        
print(len(respuesta))