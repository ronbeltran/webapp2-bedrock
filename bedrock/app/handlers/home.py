import webapp2

from app.handlers import BaseHandler


class HomeHandler(BaseHandler):
    TEMPLATE_PATH = 'index.html'

    def get(self):
        return self.render_page({
            'foo': 'bar',
        })


ROUTES = [
    webapp2.Route('/', HomeHandler, 'home'),
]
