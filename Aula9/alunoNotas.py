import cherrypy
from aluno import Aluno

class Root(object):

     @cherrypy.expose
     def index(self):
         return """
          <html>
               <head><head>
               <body style="padding:10%">
                    <h1>Formulário</h1>
                    <form method="post" action="resultado">
                         <label>Nome</label>
                         <input type="text" name="nome">
                         <label>Nota 1</label>
                         <input type="text" name="notaUm">
                         <label>Nota 2</label>
                         <input type="text" name="notaDois">
                         <label>Nota 3</label>
                         <input type="text" name="notaTres">
                         <button type="submit">Enviar</button>
                    </form>
               </body>
          </html>
          """

     @cherrypy.expose
     def hora(self):
          return str(datetime.now())

     @cherrypy.expose
     def resultado(self, nome, notaUm, notaDois, notaTres):
          aluno = Aluno(nome, notaUm, notaDois, notaTres)
          return """
          <a type="button" onClick="history.go(-1)" style="cursor:pointer">Voltar</a>
          <h1>Relatório</h1>
          <br>
          Nome : {} <br>          
          Nota 1 : {} <br>          
          Nota 2 : {} <br>          
          Nota 3 : {} <br>          
          <h2>A média das notas é {}.</h2>
          """.format(aluno.nome, aluno.notaUm, aluno.notaDois, aluno.notaTres, aluno.media())


cherrypy.tree.mount(Root(), '/')
cherrypy.config.update(
    {'server.socket_host': '0.0.0.0', 'server.socket_port': 8000, })
cherrypy.engine.start()
cherrypy.engine.block()
