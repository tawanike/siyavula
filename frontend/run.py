from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

if __name__ == '__main__':
  with Configurator() as config:
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_static_view('deform_static', 'deform:static/')
    config.scan('views')

    app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 3000, app)
  server.serve_forever()