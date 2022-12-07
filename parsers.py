# -*- coding: utf-8 -*-
'''
Created on 23 ene 2022

@author: reinaqu_2
'''

def parsea_gana_atacante(cadena) -> bool:
   
    res = None
    cadena = cadena.lower().strip()
    
    if (cadena == "win"):
        res = True
    elif (cadena == "loss"):
        res = False
    
    return res

def parsea_muertes_principales(cadena) ->bool:
    
    res = None
    cadena = cadena.strip()
    
    if (cadena == "1"):
        res = True
    elif (cadena == "0"):
        res = False
    
    return res

def parsea_comandantes(cadena):
    
    res = [cadena.strip() for cadena in cadena.split(",")]
    
    return res 

def parsea_int(cadena):
    
    res = None if cadena == "" else int(cadena)
    
    return res