import random
import string
import cherrypy


class StringGennerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, int(length)))

cherrypy.config.update({'server.socket_port': 8789})

if __name__ == '__main__':
    cherrypy.quickstart(StringGennerator())
    
# http://localhost:8789/generate?length=16