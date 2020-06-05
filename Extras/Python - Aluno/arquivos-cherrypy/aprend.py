#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#==========================================================================================
#title            :aprend.py 
#description      :Sistema de Gerenciamento Escolar Magnus
#author           :Alexandre Zanatta Vieira
#date             :20140106
#version          :0.4.0
#usage            :python aprend.py
#python_version   :2.7.3 (default, Jan  2 2013, 13:56:14)
#cherrypy_version :3.2.2
#==========================================================================================

import cherrypy
from front import inicio

### Definições da aplicação ##################
cherrypy.tree.mount(inicio(), '/', config = '/usr/bin/sges/code/ap.conf')
cherrypy.config.update(
   {'server.socket_host': '0.0.0.0',
    'server.socket_port': 3127,} )
cherrypy.engine.start()
cherrypy.engine.block()
##############################################