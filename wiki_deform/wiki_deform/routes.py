def includeme(config):
    # config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('wiki_view', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')
    config.add_static_view('deform_static', 'deform:static/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
