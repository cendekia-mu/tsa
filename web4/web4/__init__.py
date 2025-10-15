from pyramid.config import Configurator
from ziggurat_foundations.models import groupfinder
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory(
        settings['session.secret'],
    )

    authn_policy = AuthTktAuthenticationPolicy(settings['session.secret'],
                                               callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                      root_factory='web4.models.RootFactory',
                      authentication_policy=authn_policy,
                      authorization_policy=authz_policy) 
    config.include('pyramid_chameleon')
    config.include('.routes')
    config.include('.models')
    config.scan()
    config.set_session_factory(session_factory)
    return config.make_wsgi_app()
