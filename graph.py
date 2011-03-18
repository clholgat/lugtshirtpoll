import cgi
import os
import math
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'pygooglechart-0.2.1'))

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from pygooglechart import PieChart3D

from LPData import Totals
from LPData import T_Shirts
import render

def stacked_vertical():
    total = Totals.get_or_insert('total')
    if len(total.shirts) == 0:
        shirts = sorted(T_Shirts, key= lambda shirt: shirt[0])
        for shirt in shirts:
            total.shirts.append(shirt[0])
            total.votes.append(0)
    
    votes = []
    shirts = []
    i = 0
    while i < len(total.votes):
        if total.votes[i] != 0:
            votes.append(total.votes[i])
            shirts.append('Design %s' % total.shirts[i])
        i += 1
    
    if len(votes) == 0:
      return ''
      
    
    chart = PieChart3D(650, 300)
    chart.add_data(votes)
    chart.set_pie_labels(shirts)
    return chart.get_url()
    
class GraphPage(webapp.RequestHandler):
    def get(self):
        render.header(self)
        render.body(self, 'graph.html', {'chart' : stacked_vertical()})
        render.footer(self)

application = webapp.WSGIApplication([('/graph', GraphPage)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
