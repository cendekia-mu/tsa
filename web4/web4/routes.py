routes = [{"name": "home", "path": "/"},
          {"name": "login", "path": "/login", "file": "login",
              "attr": "view_login", "tpl": "form.pt"},
          {"name": "logout", "path": "/logout", "file": "login",
              "attr": "view_logout", "tpl": "form.pt"},
          {"name": "user-list", "path": "/user", "file": "users",
              "attr": "view_list", "tpl": "list_user.pt"},
          {"name": "user-create", "path": "/user/add",
              "file": "users", "attr": "view_create", "tpl": "form.pt"},
          {"name": "user-read", "path": "/user/{id}/read",
              "file": "users", "attr": "view_read", "tpl": "form.pt"},
          {"name": "user-update", "path": "/user/{id}/edit",
              "file": "users", "attr": "view_update", "tpl": "form.pt"},
          {"name": "user-delete", "path": "/user/{id}/delete",
              "file": "users", "attr": "view_delete", "tpl": "form.pt"},
          {"name": "group-list", "path": "/group", "file": "groups",
              "attr": "view_list", "tpl": "list_group.pt"},
          {"name": "group-create", "path": "/group/create",
              "file": "groups", "attr": "view_create", "tpl": "form.pt"},
          {"name": "group-read", "path": "/group/{id}/read",
              "file": "groups", "attr": "view_read", "tpl": "form.pt"},
          {"name": "group-update", "path": "/group/{id}/update",
              "file": "groups", "attr": "view_update", "tpl": "form.pt"},
          {"name": "group-delete", "path": "/group/{id}/delete",
              "file": "groups", "attr": "view_delete", "tpl": "form.pt"},

          {"name": "user-permission-list", "path": "/user/permission",
              "file": "user_permission", "attr": "view_list", "tpl": "list_group.pt"},
          {"name": "user-permission-create", "path": "/user/permission/create",
              "file": "user_permission", "attr": "view_create", "tpl": "form.pt"},
          {"name": "user-permission-read", "path": "/user/permission/{id}/read",
              "file": "user_permission", "attr": "view_read", "tpl": "form.pt"},
          {"name": "user-permission-update", "path": "/user/permission/{id}/update",
              "file": "user_permission", "attr": "view_update", "tpl": "form.pt"},
          {"name": "user-permission-delete", "path": "/user/permission/{id}/delete",
              "file": "user_permission", "attr": "view_delete", "tpl": "form.pt"},

          {"name": "group-permission-list", "path": "/group/permission",
              "file": "group_permission", "attr": "view_list", "tpl": "list_group_permission.pt"},
          {"name": "group-permission-create", "path": "/group/permission/create",
              "file": "group_permission", "attr": "view_create", "tpl": "form.pt"},
          {"name": "group-permission-read", "path": "/group/permission/{id}/read",
              "file": "group_permission", "attr": "view_read", "tpl": "form.pt"},
          {"name": "group-permission-update", "path": "/group/permission/{id}/update",
              "file": "group_permission", "attr": "view_update", "tpl": "form.pt"},
          {"name": "group-permission-delete", "path": "/group/permission/{id}/delete",
              "file": "group_permission", "attr": "view_delete", "tpl": "form.pt"},

          ]


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    for route in routes:
        config.add_route(route['name'], route['path'])
        if 'file' not in route:
            continue
        view_file = f'web4.views.{route["file"]}.Views'
        attr =route["attr"]
        renderer = f'web4:templates/{route["tpl"]}'
        try:
            config.add_view(view_file, attr=attr,
                        route_name=route['name'], renderer=renderer)
        except Exception as e:
            print(f"Error adding view for route {route['name']}: {e}")


# def includeme(config):
#     config.add_static_view('static', 'static', cache_max_age=3600)
#     config.add_route('home', '/')
#     config.add_route('login', '/login')
#     config.add_route('logout', '/logout')
#     config.add_route('user-list', '/user')
#     config.add_route('user-create', '/user/add')
#     config.add_route('user-read', '/user/{id}/read')
#     config.add_route('user-update', '/user/{id}/edit')
#     config.add_route('user-delete', '/user/{id}/delete')

#     form_tpl = 'web4:templates/form.pt'
#     view_file = 'web4.views.users.Views'
#     list_tpl = 'web4:templates/list_user.pt'
#     config.add_view(view_file, attr='view_list',
#                     route_name='user-list', renderer=list_tpl)
#     config.add_view(view_file, attr='view_create',
#                     route_name='user-create', renderer=form_tpl)
#     config.add_view(view_file, attr='view_read',
#                     route_name='user-read', renderer=form_tpl)
#     config.add_view(view_file, attr='view_update',
#                     route_name='user-update', renderer=form_tpl)
#     config.add_view(view_file, attr='view_delete',
#                     route_name='user-delete', renderer=form_tpl)

#     config.add_route('group-list', '/group')
#     config.add_route('group-create', '/group/create')
#     config.add_route('group-read', '/group/{id}/read')
#     config.add_route('group-update', '/group/{id}/update')
#     config.add_route('group-delete', '/group/{id}/delete')

#     view_file = 'web4.views.groups.Views'
#     list_tpl = 'web4:templates/list_group.pt'
#     config.add_view(view_file, attr='view_list',
#                     route_name='group-list', renderer=list_tpl)
#     config.add_view(view_file, attr='view_create',
#                     route_name='group-create', renderer=form_tpl)
#     config.add_view(view_file, attr='view_read',
#                     route_name='group-read', renderer=form_tpl)
#     config.add_view(view_file, attr='view_update',
#                     route_name='group-update', renderer=form_tpl)
#     config.add_view(view_file, attr='view_delete',
#                     route_name='group-delete', renderer=form_tpl)
