from pyramid.authorization import (
    Allow,
    Everyone,
)
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPSeeOther,
)

from . import models


def includeme(config):
    config.add_route('view_wiki', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('deform_static', 'deform:static/')
    config.scan('.views')