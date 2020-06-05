import cherrypy

from root import Root

### Definições da aplicação ##################
cherrypy.tree.mount(Root(), '/', config="projeto.conf")
cherrypy.config.update(
   {'server.socket_host': '0.0.0.0',
    'server.socket_port': 3127,} )
cherrypy.engine.start()
cherrypy.engine.block()
##############################################