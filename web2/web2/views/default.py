from pyramid.view import view_config


@view_config(route_name='home', renderer='web2:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'web2'}

@view_config(route_name='contact', renderer='web2:templates/contact.pt')
def contact_view(request):
    return {'project': 'web2'}
