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
import codigo.test as t
import subprocess
import json

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

################################################################################

def crear_hyper():

    '''
    # formato es el arreglo que contiene la informacion del sismo: latitud, longitud, comentario etc...
    # sentido es el valor dado al checkbox sentido para saber si el sismo fue sentido o no y publicarlo
    # en la pagina
    # paths es la variable que contiene las rutas necesarias para el programa
    '''
    '''aqui se crea el archivo en seisan con comentario'''
    # fc.insertar_comentario(paths,formato,sentido)
    # fc.guardar_datos(paths,formato)
    # sentido = formato['sentido']
    print(text_id.get())
    id = text_id.get()
    paths = open("utiles/paths.txt").readlines()
    formato = t.formato(id)
    fc.guardar_datos(paths,formato)
    
   
    sentido=True



#parte que crea la aplicacion grafica
root = tk.Tk()
root.title('Hyper')
root.geometry('400x220')
root.resizable(width=False, height=False)
font_size = font.Font(weight='bold',size=14)
mag_var = tk.IntVar()
text_id = tk.StringVar()
backcolor='white smoke'
root.configure(background=backcolor)
font_size=17

boton = tk.Button(root,text='Enviar Datos',font=font_size,background='forest green',
                  foreground='yellow',command=crear_hyper)
etiqueta3 = tk.Label(root,text='Id ',font=font_size)
id_textbox = tk.Entry(root,width=12,textvariable=text_id)

etiqueta3.grid(row=3,column=2)
id_textbox.grid(row=3,column=3)
boton.grid(row=9,column=3)
# en un futuro se creara una etiqueta status donde se vera el status de la app
# etiqueta_status.grid(row=13,column=0)
# status.grid(row=13,column=1)

root.mainloop()
