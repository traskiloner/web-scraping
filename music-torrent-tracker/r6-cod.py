#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
# URLS a dia 18 - Febrero - 2016 son 5784
# Esta version añade al xml lineas de autores repetidas

import urllib2
from time import time
from lxml import etree

url_general = "http://music-torrent.net/"

print "Introduzca 1 para generar un fichero de URLs"
print "Introduzca 2 para generar un fichero XML"
# print "introduzca 3 para obtener todos los ficheros torrents"

opcion = raw_input("Opción: ")

if opcion == "1":

    hora_inicio = time()
    numero = 2
    url_numero = url_general
    lista_urls = []
    primera_vuelta = True


    def comprueba_url(url):
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

    print "Todas las URLs de la web conseguidas,son:", len(lista_urls)
    print "Ha transcurrido", time() - hora_inicio, "segundos"

    fichero_urls = open("fichero_urls.txt", "w")

    for web in lista_urls:
        fichero_urls.write(web + '\n')
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


        def comprueba_url(url):
            try:
                respuesta = urllib2.urlopen(url)
                return respuesta
            except:
                return "error"


        musica = etree.Element("musica")
        doc_musica = etree.ElementTree(musica)
        autores = []
        ndisco = 0
        for url in lista_urls[:204]:

            print ndisco
            ndisco += 1

            if comprueba_url(url) != "error":
                html = comprueba_url(url).readlines()
                numero_linea = 0

                for a in html:
                    numero_linea = numero_linea + 1

                    if numero_linea == 66:
                        # print "Autor", a.strip()[:-5]
                        if a.strip()[:-5] in autores:
                            print "Autor repetido: ", a.strip()[:-5]
                            autor = etree.SubElement(musica, "autor")
                            autor.text = a.strip()[:-5]
                            autores.append(a.strip()[:-5])
                        else:
                            autor = etree.SubElement(musica, "autor")
                            autor.text = a.strip()[:-5]
                            autores.append(a.strip()[:-5])

                    if numero_linea == 71:
                        anyo = a.strip()

                    if numero_linea == 74:
                        # print "Album: ",a.strip()[:-5]
                        album = etree.SubElement(autor, "album")
                        album.text = a.strip()[:-5]
                        album.attrib['anyo'] = anyo

                    if numero_linea >= 97 and a.strip().startswith('<li>'):
                        nombre_cancion = a.strip()[4:-5]
                        #print "Antes de: ", nombre_cancion
                        #if "´s" in nombre_cancion:
                        #    nombre_cancion = nombre_cancion.replace("´s", "'s")
                            # print "Despues de: ", nombre_cancion
                        #elif "’s" in nombre_cancion:
                        #    nombre_cancion = nombre_cancion.replace("’s", "'s")
                        #elif "ï" in nombre_cancion:
                        #    nombre_cancion = nombre_cancion.replace("ï", "i")
                        #elif "é" in nombre_cancion:
                        #    nombre_cancion = nombre_cancion.replace("é", "e")
                        cancion = etree.SubElement(album, "cancion")
                        cancion.text = unicode(nombre_cancion,'utf-8')

                    if numero_linea >= 103 and a.strip().startswith('<a class="btn btn-lg btn-success'):
                        # print "Fichero torrent: ",url_general + a.strip()[65:-2]
                        torrent = etree.SubElement(album, "url_torrent")
                        torrent.text = url_general + a.strip()[65:-2]

    arbol = etree.tostring(doc_musica, pretty_print=True, xml_declaration=True, encoding="utf-8")

    xml_musica = open("musica.xml", "w")
    xml_musica.write(arbol)
    xml_musica.close()
    print autores