import webapp2
import jinja2

import config
from app.handlers import BaseHandler
from app.utils.jinja import JINJA_ENV


class HomeHandler(BaseHandler):
    TEMPLATE_PATH = 'index.html'

    def get(self):
        return self.render_page({
            'foo': 'bar',
        })


app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, 'home')
], debug=config.DEBUG)
