import os

import webapp2
import jinja2

import config


JINJA_ENV = jinja2.Environment(
    autoescape=lambda x: True,
    extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader(
        os.path.join(config.PROJECT_ROOT, 'templates')),
)


JINJA_ENV.globals.update({'uri_for': webapp2.uri_for})
