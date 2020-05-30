import cherrypy
from datetime import datetime

class Root(object):

     @cherrypy.expose
     def index(self):
          return """
          <html>
               <head><head>
               <body style="padding:10%">
                    <h1>Formulário</span>
                    <form method="post" action="resultado">
                         <input type="text" name="numero">
                         <button type="submit">Enviar</button>
                    </form>
               </body>
          </html>
          """

     @cherrypy.expose
     def hora(self):
          return str(datetime.now())

     @cherrypy.expose
     def resultado(self, numero):
          return """Você digitou {}""".format(numero)

cherrypy.tree.mount(Root(), '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8000, })
cherrypy.engine.start()
cherrypy.engine.block()
