import cherrypy

class Root(object):

     @cherrypy.expose
     def index(self):
         return """
          <html>
               <head><head>
               <body style="padding:10%">
                    <h1>Formulário</h1>
                    <form method="post" action="resultado">
                         <span>Nome</span>
                         <input type="text" name="nome">
                         <span>Idade</span>
                         <input type="text" name="idade">
                         <span>Telefone</span>
                         <input type="text" name="telefone">
                         <button type="submit">Enviar</button>
                    </form>
               </body>
          </html>
          """

     @cherrypy.expose
     def hora(self):
          return str(datetime.now())

     @cherrypy.expose
     def resultado(self, nome, idade, telefone):
          return """
          <h1>{}, você tem {} anos e seu telefone é {}.</h1>
          <a type="button" onClick="history.go(-1)" style="cursor:pointer">Voltar</a>
          """.format(nome,idade,telefone)


cherrypy.tree.mount(Root(), '/')
cherrypy.config.update(
    {'server.socket_host': '0.0.0.0', 'server.socket_port': 8000, })
cherrypy.engine.start()
cherrypy.engine.block()
