from pyramid.view import notfound_view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPSeeOther

@notfound_view_config(renderer='web4:templates/404.pt')
def notfound_view(request):
    request.response.status = 404
    return {}


@forbidden_view_config(renderer='templates/403.pt')
def forbidden_view(request):
    if not request.is_authenticated:
        next_url = request.route_url(
            'login', _query={'came_from': request.url})
        return HTTPSeeOther(location=next_url)

    request.response.status = 403
    return {"url": request.url}
