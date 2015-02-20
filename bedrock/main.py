import webapp2
import jinja2

import config
from app.utils.jinja import JINJA_ENV


class BaseHandler(webapp2.RequestHandler):
    TEMPLATE_PATH = None

    def render_page(self, extra_context=None, template=None):
        if template is None:
            template = self.TEMPLATE_PATH
        context = getattr(self, 'context', {})
        if extra_context:
            context.update(extra_context)
        assert template, 'TEMPLATE_PATH not defined'
        template = JINJA_ENV.get_template(template)
        return self.response.out.write(template.render(context))


class HomeHandler(BaseHandler):
    TEMPLATE_PATH = 'index.html'

    def get(self):
        return self.render_page({
            'foo': 'bar',
        })


app = webapp2.WSGIApplication([
    webapp2.Route('/', HomeHandler, 'home')
], debug=config.DEBUG)
