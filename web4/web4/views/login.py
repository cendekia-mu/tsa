
from pyramid.view import view_config


@view_config(route_name='login', renderer='web4:templates/login.pt')
def login(request):
    return {"came_from": request.params.get("came_from", "/")}
