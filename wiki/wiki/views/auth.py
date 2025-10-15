from pyramid.csrf import new_csrf_token
from pyramid.httpexceptions import HTTPSeeOther
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    forbidden_view_config,
    view_config,
)
import logging
from .. import models

_logging = logging.getLogger(__name__)

class LoginSchema(colander.Schema):
    login = colander.SchemaNode(
        colander.String(),
        title="Login",
        description="Your login name",
    )
    password = colander.SchemaNode(
        colander.String(),
        title="Password",
        description="Your password",
        widget=deform.widget.PasswordWidget(),
    )

@view_config(route_name='login', renderer='wiki:templates/login.jinja2')
def login(request):
    _logging.info("View login called")
    # x = "Contoh Print"
    next_url = request.params.get('next', request.referrer)
    if not next_url:
        next_url = request.route_url('view_wiki')
    if request.identity is not None:
        return HTTPSeeOther(location=next_url)
    
    message = ''
    login = ''
    if request.method == 'POST':
        login = request.params['login']
        password = request.params['password']
        user = (
            request.dbsession.query(models.User)
            .filter_by(name=login)
            .first()
        )
        if user is not None and user.check_password(password):
            new_csrf_token(request)
            headers = remember(request, user.id)
            return HTTPSeeOther(location=next_url, headers=headers)
        message = 'Failed login'
        request.response.status = 400

    return dict(
        message=message,
        url=request.route_url('login'),
        next_url=next_url,
        login=login,
    )


@view_config(route_name='logout')
def logout(request):
    next_url = request.route_url('view_wiki')
    if request.method == 'POST':
        new_csrf_token(request)
        headers = forget(request)
        return HTTPSeeOther(location=next_url, headers=headers)

    return HTTPSeeOther(location=next_url)


@forbidden_view_config(renderer='wiki:templates/403.jinja2')
def forbidden_view(exc, request):
    if not request.is_authenticated:
        next_url = request.route_url('login', _query={'next': request.url})
        return HTTPSeeOther(location=next_url)

    request.response.status = 403
    return {}
