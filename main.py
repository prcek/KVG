import webapp2
from base import BaseHandler


class MainPage(BaseHandler):
    def get(self):
        context = {'name': 'webapp2 test'}
        self.render_response('index.html',**context)



app = webapp2.WSGIApplication([
    (r'/', MainPage),
    ],
    debug=True)