#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

import urllib2
url = "http://music-torrent.net/"
lista_urls =[]

def comprueba_url (url):
    try:
        respuesta = urllib2.urlopen(url)
        return respuesta
    except:
        respuesta = urllib2.urlopen(url)
        return "error"

while comprueba_url(url) != "error":
    print url
    html = comprueba_url(url).readlines()
    lista = []
    for a in html:
        if a.strip().startswith("<a href"):
            lista.append(a.strip())

    lista = lista[14:-1]
    for i in lista:
        lista_urls.append(url + i.split(" ")[1][7:-1])

    print lista_urls
    if url.endswith([0-9]):
        url = url + "1"
    else:
        url = url + "2"
    print url