from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    # Memanggil URL http://localhost:6543/?name=Alice&address=Jakarta
    url = request.url
    name = request.params.get('name', 'No Name Provided')
    address = request.params.get('address', 'No Address Provided')
    
    response = f"Url: {url}<br>"
    response += f"Hello: {name}<br>"
    response += f"Address: {address}<br>"

    return Response(response)

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(hello_world, route_name='home')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
