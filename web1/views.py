from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from html import escape


# First view, available at http://localhost:6543/
@view_config(route_name='home', renderer='templates/home.pt')
def home_view(request):
    # return Response('<p>Visit <a href="/howdy?name=lisa">hello</a></p>')
    return {"today": "a beautiful day", "name": "Lisa", "date": "2024-06-12"}


# /howdy?name=alice which links to the next view
@view_config(route_name='hello')
def hello_view(request):
    name = request.params.get('name', 'No Name')
    # body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
    # Python html.escape to prevent Cross-Site Scripting (XSS) [CWE 79]
    # return Response(body % escape(name))

    # body = f'<p>Hi {escape(name)}, this <a href="/goto">redirects</a></p>'
    # return Response(body)
    
    # return Response(f'<p>Hi {escape(name)}, this <a href="/goto">redirects</a></p>')
    
    body = '<p>Hi {name}, this <a href="/goto">redirects</a></p>'
    return Response(body.format(name=escape(name)))


# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")


# /problem which causes a site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()


@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return { "data": [1, 2, 3] }
