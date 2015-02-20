import webapp2
import jinja2

import config

import app.handlers.home

ROUTES = []

ROUTES += app.handlers.home.ROUTES

app = webapp2.WSGIApplication(ROUTES, debug=config.DEBUG)
