#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

import urllib2
url = "http://music-torrent.net/"
lista_urls =[]

respuesta= urllib2.urlopen(url)
html = respuesta.readlines()

lista = []
for a in html:
    if a.strip().startswith("<a href"):
        lista.append(a.strip())

lista = lista[14:-1]
for i in lista:
    lista_urls.append(url + i.split(" ")[1][7:-1])

print lista_urls