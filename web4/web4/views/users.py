import logging
import colander
import datetime
import deform
from pyramid.view import view_config
from ..models import User
from web4.views import BaseViews

log = logging.getLogger(__name__)

class CreateSchema(colander.MappingSchema):
    user_name = colander.SchemaNode(
        colander.String(),
        title="Username",
        description="Enter your username",
    )
    email = colander.SchemaNode(
        colander.String(),
        title="Email",
        validator=colander.Email(),
        description="Enter your email address",
    )
    password = colander.SchemaNode(
        colander.String(),
        title="Password",
        description="Enter your password",
        widget=deform.widget.PasswordWidget(),
    )

class UpdateSchema(CreateSchema):
    id = colander.SchemaNode(
        colander.Integer(),
        title="ID",
        description="Unique identifier for the user",
        missing=colander.drop,
        widget=deform.widget.HiddenWidget(),
    )


class ReadSchema(UpdateSchema):
    def after_bind(self, node, kw):
        for child in node.children:
            child.widget.readonly = True
            child.missing = colander.drop

class Views(BaseViews):
    def __init__(self, request):
        super().__init__(request)
        self.table = User  
        self.CreateSchema = CreateSchema  
        self.UpdateSchema = UpdateSchema  
        self.ReadSchema = ReadSchema
        self.list_route_name = 'user-list'

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

    def save(self, values, row=None):
        if not row:
            values["registered_date"] = datetime.datetime.now()
        row = super().save(values, row)
        if values.get('password'):
            row.set_password(values['password'])
        return row

    # @view_config(route_name='user-create', renderer='web4:templates/form.pt')
    # def view_create(self):
    #     return super().view_create()

    # @view_config(route_name='user-read', renderer='web4:templates/form.pt')
    # def view_read(self):
    #     return super().view_read()

    # @view_config(route_name='user-update', renderer='web4:templates/form.pt')
    # def view_update(self):
    #     return super().view_update()

    # @view_config(route_name='user-list', renderer='web4:templates/list_user.pt')
    # def view_list(self):
    #     return super().view_list()

    # @view_config(route_name='user-delete', renderer='web4:templates/form.pt')
    # def view_delete(self):
    #     return super().view_delete()
