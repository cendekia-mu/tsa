from pyramid.config import Configurator
import logging 
log = logging.getLogger(__name__)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    log.info("Starting web2 application...")
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.scan()
        log.info("Configuration complete, application is ready.")
    return config.make_wsgi_app()
