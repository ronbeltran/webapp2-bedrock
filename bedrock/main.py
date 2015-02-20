import webapp2
import jinja2


JINJA_ENV = jinja2.Environment(
    autoescape=lambda x: True,
    extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader('templates'),
)

JINJA_ENV.globals.update({'uri_for': webapp2.uri_for})


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
], debug=True)
