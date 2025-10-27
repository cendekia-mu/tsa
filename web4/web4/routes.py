def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('user', '/user')
    config.add_route('user-add', '/user/add')
    config.add_route('user-edit', '/user/{id}/edit')
    config.add_route('user-delete', '/user/{id}/delete')
