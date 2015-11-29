import cherrypy
import random

class Details(object):
    def __init__(self):
       self.login = Login()
       self.orders = Orders()
       print 'SimpleTen Edit Started...'


    @cherrypy.expose()
    def newstext(self):
        print 'Gathering Intelligence...'
        return 'enter any user & pass click login \n or just click login \n Edit by iSimpleTen'

    @cherrypy.expose()
    def checkip(self):
        print 'Patching Online Check...'
        return '<html><head><title>Current IP Check</title></head><body>Current IP Address: 0.0.0.0</body></html>'


    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            print 'Gathering Information...'
            cherrypy.request.params['uin'] = vpath.pop(0)
            vpath.pop(0)
            cherrypy.request.params['pass'] = vpath.pop(0)
            cherrypy.request.params['hash'] = vpath.pop(0)
            cherrypy.request.params['eip'] = vpath.pop(0)
            return self.login

        if len(vpath) == 2:
             cherrypy.request.params['uin'] = vpath.pop(0)
             return self.orders


        return vpath

class Login(object):
    @cherrypy.expose
    def index(self, uin, password, hash, eip):
        print 'Generating Order Number...'
        num = random.randint(100,999)
        return '%s' % num

class Orders(object):
    @cherrypy.expose()
    def index(self, uin):
        print 'Your Order #%s' % uin
        return 'completed'


if __name__ == '__main__':
    cherrypy.config.update({'environment' : 'production'})
    cherrypy.quickstart(Details())