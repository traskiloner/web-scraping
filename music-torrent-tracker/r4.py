#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

import urllib2
from time import time
hora_inicio = time()
url = "http://music-torrent.net/"
numero = 2
url_numero = url

lista_urls =[]
primera_vuelta = True

def comprueba_url (url):
    try:
        respuesta = urllib2.urlopen(url)
        return respuesta
    except:
        return "error"

while comprueba_url(url_numero) != "error":

    html = comprueba_url(url_numero).readlines()
    lista = []
    for a in html:
        if a.strip().startswith("<a href"):
            lista.append(a.strip())

    lista = lista[14:-1]


    if primera_vuelta is True:
        for i in lista:
            lista_urls.append(url + i.split(" ")[1][7:-1])
        primera_vuelta = False
    else:
        for i in lista[:-1]:
            lista_urls.append(url + i.split(" ")[1][7:-1])

    if url_numero[-1].isdigit():
        numero = numero + 1
        url_numero = url + str(numero)
    else:
        url_numero = url + str(numero)

print "Todas las URLs de la web conseguidas,son:"len(lista_urls)
print "Ha transcurrido", time() - hora_inicio, "segundos"