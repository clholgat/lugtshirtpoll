import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from LPData import Lugger

class MainPage(webapp.RequestHandler):
    def get(self):
        loggedIn = users.get_current_user()
        lugger = Lugger.get_or_insert(loggedIn.user_id())
        
        if lugger.voted == True:
            self.redirect('/graph')
        else:
            self.redirect('/vote')
            
application = webapp.WSGIApplication([('/.*', MainPage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
