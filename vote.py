import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from LPData import Lugger
from LPData import T_Shirts
from LPData import Totals
import render

class VotePage(webapp.RequestHandler):    
    def get(self):
        loggedIn = users.get_current_user()
        lugger = Lugger.get_or_insert(loggedIn.user_id())
        
        if lugger.voted == True:
            self.redirect('/graph')    
        
        shirts_tmp = sorted(T_Shirts, key= lambda shirt: shirt[0])
        shirts = []
        for shirt in shirts_tmp:
            if lugger.votes.count(shirt[0]) == 0:
                shirts.append(shirt)
        
        render.header(self)
        if len(lugger.votes) == 0:
            render.body(self, 'intro.html', {'user' : loggedIn.nickname})
            render.body(self, 'display.html', {'shirts' : shirts, 
                                               'rank' : '', 
                                               'id': loggedIn.user_id()})
        elif len(lugger.votes) == 1:
            render.body(self, 'display.html', {'shirts' : shirts, 
                                               'rank' : 'second', 
                                               'id': loggedIn.user_id()})
        elif len(lugger.votes) == 2:
            render.body(self, 'display.html', {'shirts' : shirts, 
                                               'rank' : 'third', 
                                               'id': loggedIn.user_id()})
        elif len(lugger.votes) == 3:
            lugger.voted = True
            lugger.put()
            self.redirect('/graph')
        
        render.footer(self)
            
    def post(self):
        lugger = Lugger.get_by_key_name(self.request.get('id'))
        vote = int(self.request.get('vote'))
        if lugger.votes.count(vote) == 0:
            total = Totals.get_or_insert('total')
            lugger.votes.append(vote)
            if len(total.shirts) == 0:
                shirts = sorted(T_Shirts, key= lambda shirt: shirt[0])
                for shirt in shirts:
                    total.shirts.append(shirt[0])
                    total.votes.append(0)                    
            total.votes[total.shirts.index(vote)] += (4-len(lugger.votes))
            total.put()
            lugger.put()
        self.redirect('/vote')
    
application = webapp.WSGIApplication([('/vote', VotePage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
