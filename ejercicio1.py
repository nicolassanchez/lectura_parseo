# -*- coding: utf-8 -*-
'''
Created on 22 ene 2022

@author: lsi 
'''
from collections import namedtuple, Counter
from src.parsers import *
import csv
 

BatallaGOT = namedtuple('BatallaGOT', 'nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados')

### EJERCICIO 1  - 25 minutos
def lee_batallas (fichero):
    
    res = []
    
    with open(fichero, encoding='utf-8') as f:
        
        lector = csv.reader(f, delimiter=',')
        next(lector)
    
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, \
                    comandantes_atacantes, comandantes_atacados, region, num_atacantes, \
                    num_atacados in lector:
        
            gana_atacante         = parsea_gana_atacante(gana_atacante)
            muertes_principales   = parsea_muertes_principales(muertes_principales)
            comandantes_atacados  = parsea_comandantes(comandantes_atacados)
            comandantes_atacantes = parsea_comandantes(comandantes_atacantes)
            num_atacantes         = parsea_int(num_atacantes)
            num_atacados          = parsea_int(num_atacados)
            
            res.append(BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, \
                                  muertes_principales, comandantes_atacantes, comandantes_atacados, \
                                  region, num_atacantes, num_atacados))
            
    return res      
