# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:03:02 2019

@author: el_in
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 11:50:37 2017
version 1.2

@author: Cgrs scripts
"""


import sys
import os
import os.path
import codigo.funciones_sismicas2 as fc
import json
import subprocess

PYTHON_VERSION = sys.version_info.major

PYTHON_VERSION

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("se requiere el modulo tkinter")
from tkinter import font


#print (json.dumps(obj))
# print(obj)
def formato(id):
    # with open("formato.txt",'r') as texto:
    
    cmd = f"scbulletin -d postgresql://sysop@localhost/seiscomp3 -E {id}".split()
    shell_cmd = subprocess.run((cmd), capture_output=True, text=True)
    texto = shell_cmd.stdout
    
    a = texto.read()[150:250]
    path_provincias = 'provinciascsv'
    path_ciudades = 'utiles/localidades_2mundo.dat'

    ciudades = fc.get_ciudades(path_ciudades)

    l = a.split()
    mag = float(l[2][2:]) - .3
    date = l[3]
    fecha = date.replace('/',"-")
    hora = l[4]
    lat = float(l[5])
    lon = float(l[7])*-1
    deph = l[9]
    i_d = fecha.replace('-','')+hora.replace(':','')
    comentario = fc.generar_comentario(ciudades,lat,lon,path_provincias)

    # salida  = i_d+'  '+fecha+'  '+hora+'  '+lat+'  '+lon+'  '+deph+'  '+mag
    salida = f'{i_d[:-4]}  {fecha}  {hora}  {lat}  {lon}  {deph}  {mag}'
    obj = {'id':i_d,
        'analista':"Carlos",
        "fecha":fecha,
        "hora":hora,
        "lat":lat,
        "lon":lon,
        "depth":deph,
        "mag":mag,
        "magC":mag,
        "rms":"0.8",
        "magL":mag,
        "magW":mag,
        "comentario":comentario,
        "salida":salida,
        "tipo_magni":"mw",
        "gapInfo":"",
        "focalInfo":"",
        'sentido':True,
        'data_estaciones':"",
    }
    print(obj)

    return obj
# formato = formato()
