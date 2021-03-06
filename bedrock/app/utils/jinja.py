import os

import webapp2
import jinja2

import config
from app.utils.compressor import WEBASSETS_ENV


JINJA_ENV = jinja2.Environment(
    autoescape=lambda x: True,
    extensions=['jinja2.ext.autoescape',
                'webassets.ext.jinja2.AssetsExtension'],
    loader=jinja2.FileSystemLoader(
        os.path.join(config.PROJECT_ROOT, 'templates')),
)


JINJA_ENV.globals.update({'uri_for': webapp2.uri_for})
JINJA_ENV.assets_environment = WEBASSETS_ENV
