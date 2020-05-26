import cherryPy
import os.path

class tutorial:
     def index(self):
          output = '''
          Olá, clique <a href='Olá'>Aqui</a> or <br>
          <form action='olanome' method='GET'>
          Seu nome
          <input type='text' name='name'>
          <input type='submit'>
          </form>
          '''
          return output
     index.exposed = True

     def ola(self):
          output = '''
          Essa é a página de boas vindas
          '''
          return output
     ola.exposed = True

     def olanome(self, name=None):
          if name:
               output='Olá %s !' % name
          else:
               output='Você precisa inserir um nome!'
          return output
     olanome.exposed = True

configfile = os.path.join(os.path.dirname(__file__),'server.config')
cherryPsy.quickstart(tutorial(),config=configfile)