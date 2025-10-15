from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('.security')
    config.include('.routes')
    config.include('.models')
    config.scan()
    return config.make_wsgi_app()
