#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
#URLS a dia 18 - Febrero - 2016 son 5784
import urllib2
from time import time
url_general = "http://music-torrent.net/"
print "Introduzca 1 para generar un fichero de URLs"
print "Introduzca 2 para generar un fichero XML"
print "Introduzca 3 para obtener todos los ficheros torrents"
print "Introduzca 4 para buscar un album dentro del fichero XML"
opcion = raw_input("Opción: ")

if opcion == "1":
    hora_inicio = time()

    numero = 2
    url_numero = url_general

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
                lista_urls.append(url_general + i.split(" ")[1][7:-1])
            primera_vuelta = False
        else:
            for i in lista[:-1]:
                lista_urls.append(url_general + i.split(" ")[1][7:-1])

        if url_numero[-1].isdigit():
            numero = numero + 1
            url_numero = url_general + str(numero)
        else:
            url_numero = url_general + str(numero)

    print "Todas las URLs de la web conseguidas,son:",len(lista_urls)
    print "Ha transcurrido", time() - hora_inicio, "segundos"
    fichero_urls = open("fichero_urls.txt","w")
    for web in lista_urls:
        fichero_urls.write(web+'\n')
    fichero_urls.close()

elif opcion == "2":
    def hay_fichero():
        try:
            fichero_urls = open("fichero_urls.txt")
        except:
            return "error"

    if hay_fichero() == "error":
        print "No se ha encontrado el fichero con las URLs"
    else:
        fichero_urls = open("fichero_urls.txt")
        lista_urls = fichero_urls.readlines()
        lista = []
        def comprueba_url (url):
            try:
                respuesta = urllib2.urlopen(url)
                return respuesta
            except:
                return "error"
        dic_autores = {"autor": "","albunes":[]}
        for url in lista_urls:
            print url

            if comprueba_url(url) != "error":
                html = comprueba_url(url).readlines()
                dic_album = {"titulo":"", "año":"","tracklist":[],"url":"", "url_torrent":""}
                numero_linea = 0

                for a in html:
                    numero_linea = numero_linea + 1

                    if numero_linea == 66:
                        print "Autor: ",a.strip()[:-5]
                        if a.strip()[:-5] not in dic_autores.values():
                            dic_autores["autor"] = a.strip()[:-5]
                    if numero_linea == 71:
                        print "Año: ",a.strip()

                    if numero_linea == 74:
                        print "Album: ",a.strip()[:-5]

                    if numero_linea >= 102 and a.strip().startswith('<li>'):
                        print "Cancion: ",a.strip()[4:-5]

                    if numero_linea >= 103 and a.strip().startswith('<a class="btn btn-lg btn-success'):
                        print "Fichero torrent: ",url_general + a.strip()[65:-2]

elif opcion == "3":
    print "Opcion 3"
