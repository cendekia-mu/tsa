import datetime
import logging
from wsgiref.validate import validator
import colander
import deform
import deform.widget
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from ..models import User

log = logging.getLogger(__name__)

class UserSchema(colander.MappingSchema):
    user_name = colander.SchemaNode(
        colander.String(),
        title="Username",
        description="Enter your username",
    )
    email = colander.SchemaNode(
        colander.String(),
        title="Email",
        description="Enter your email address",
    )
    password = colander.SchemaNode(
        colander.String(),
        title="Password",
        description="Enter your password",
        widget=deform.widget.PasswordWidget(),
    )


class Views(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='user', renderer='web4:templates/list_user.pt',
                 #  permission='view'
                 )
    def list_users(self):
        # Logic to fetch all users from the database goes here
        users = self.request.dbsession.query(User).all()
        return {'users': users}

    def save(self, values, row=None):
        if not row:
            row = User()
            row.registered_date = datetime.datetime.now()

        row.user_name = values['user_name']
        row.email = values['email']
        self.request.dbsession.add(row)
        self.request.dbsession.flush()
        if values.get('password'):
            row.set_password(values['password'])
        return row

    @view_config(route_name='user-add', renderer='web4:templates/form.pt')
    def add_user(self):
        schema = UserSchema(validator=self.form_validator)
        form = deform.Form(schema, buttons=('save', 'cancel'))

        if self.request.POST:
            if 'save' in self.request.POST:
                controls = self.request.POST.items()
                try:
                    appstruct = form.validate(controls)
                    # Logic to add user to the database goes here
                    self.save(appstruct)
                    self.request.session.flash('User added successfully!')
                except deform.ValidationFailure as e:
                    return {'form': e.render()}

            return HTTPFound(location=self.request.route_url('user'))

        rendered_form = form.render()
        return {'form': rendered_form}

    def form_validator(self, form, value):
        # Custom validation logic can be added here
        exc = colander.Invalid(
            form,
            'Terjadi kesalahan pengisian data'
        )
    
        user_id = self.request.matchdict.get('id')
        found = self.request.dbsession.query(User).filter(
            User.user_name == value['user_name']
        ).first()
        if found:
            if user_id and found.id != int(user_id):
                exc["user_name"] = 'Username already exists.'
                raise exc
            elif not user_id:
                exc["user_name"] = 'Username already exists.'
                raise exc

        found = self.request.dbsession.query(User).filter(
            User.email == value['email']
        ).first()
        if found:

            if user_id and found.id != int(user_id):
                exc["email"] = 'Email already exists.'
                raise exc
            else:
                exc["email"] = 'Email already exists.'
                raise exc

    def query_id(self):
        user_id = self.request.matchdict.get('id')
        return self.request.dbsession.query(User).filter(User.id == user_id)

    @view_config(route_name='user-edit', renderer='web4:templates/form.pt')
    def edit_user(self):
        # Logic to fetch user data from the database goes here
        query = self.query_id()
        user = query.first()
        if not user:
            self.request.session.flash('User not found!')
            return HTTPFound(location=self.request.route_url('user'))

        schema = UserSchema(validator=self.form_validator)
        form = deform.Form(schema, buttons=('save', 'cancel'))
        if self.request.POST:
            if 'save' in self.request.POST:
                controls = self.request.POST.items()
                try:
                    appstruct = form.validate(controls)
                    # Logic to update user in the database goes here
                    user = self.save(appstruct, user)
                    self.request.session.flash('User updated successfully!')
                    return HTTPFound(location=self.request.route_url('user'))
                except deform.ValidationFailure as e:
                    return {'form': e.render()}

            return HTTPFound(location=self.request.route_url('user'))

        # Pre-fill form with existing user data
        appstruct = dict(user.__dict__)
        # Remove SQLAlchemy internal state
        appstruct.pop('_sa_instance_state', None)
        rendered_form = form.render(appstruct)
        return {'form': rendered_form}

    @view_config(route_name='user-delete', renderer='web4:templates/form.pt')
    def delete_user(self):
        # Logic to fetch user data from the database goes here
        query = self.query_id()
        user = query.first()
        if not user:
            self.request.session.flash('User not found!')
            return HTTPFound(location=self.request.route_url('user'))

        schema = UserSchema()
        form = deform.Form(schema, buttons=('delete', 'cancel'))
        if self.request.POST:
            if 'delete' in self.request.POST:
                try:
                    query.delete()
                    self.request.session.flash('User deleted successfully!')
                except deform.ValidationFailure as e:
                    return {'form': e.render()}

            return HTTPFound(location=self.request.route_url('user'))

        # Pre-fill form with existing user data
        appstruct = dict(user.__dict__)
        # Remove SQLAlchemy internal state
        appstruct.pop('_sa_instance_state', None)
        rendered_form = form.render(appstruct)
        return {'form': rendered_form}
