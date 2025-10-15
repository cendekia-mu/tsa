from pyramid.config import Configurator
import logging

_logging = logging.getLogger(__name__)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    _logging.info("Starting up...")
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.security')
        config.include('.routes')
        config.include('.models')
        config.scan()
    return config.make_wsgi_app()
