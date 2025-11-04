
import logging
import colander
import deform
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models.auth import GroupPermission, Group
from web4.views import BaseViews

log = logging.getLogger(__name__)


class Permission(colander.Schema):
            permission = colander.SchemaNode(colander.String())

class Permissions(colander.SequenceSchema):
            permission = Permission()



class CreateSchema(colander.MappingSchema):
    group_id = colander.SchemaNode(
        colander.Integer(),
        title="Group Name",
        description="Group Name",
        widget = deform.widget.SelectWidget(values=[]),
    )

    perm_names = Permissions(
        widget=deform.widget.SequenceWidget(orderable=True)
    )

    # perm_name = colander.SchemaNode(
    #     colander.String(),
    #     title="Permission Name",
    #     description="Name of the permission",
    # )

    def after_bind(self, node, kw):
        # Populate group_id choices dynamically
        request = kw.get('request')
        if request:
            groups = request.dbsession.query(Group).all()
            group_choices = [(str(group.id), group.group_name) for group in groups]
            for child in node.children:
                if child.name == 'group_id':
                    child.widget.values = group_choices


class UpdateSchema(CreateSchema):
    id = colander.SchemaNode(
        colander.Integer(),
        title="ID",
        description="Unique identifier for the group",
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
        self.table = GroupPermission
        self.CreateSchema = CreateSchema
        self.UpdateSchema = UpdateSchema
        self.ReadSchema = ReadSchema
        self.list_route_name = 'group-permission-list'

    def query_id(self):
        id_ = self.request.matchdict.get('id')
        return self.request.dbsession.query(self.table).filter(self.table.group_id == id_)
    
    def form_validator(self, form, value):
        # Custom validation logic can be added here
        exc = colander.Invalid(
            form,
            'Terjadi kesalahan pengisian data'
        )

        # id_ = self.request.matchdict.get('id')
        # found = self.request.dbsession.query(self.table).filter(
        #     self.table.group_name == value['group_name'],
        #     self.table.id != id_ if id_ else True
        # ).first()
        # if found:
        #     exc["group_name"] = 'Group name already exists.'
        #     raise exc

    def save(self, values, row=None):
        #return super().save(values, row)
        if row:
            # First, delete existing permissions for the group
            self.query_id().delete()

        # Then, add the new set of permissions
        for perm in values['perm_names']:
            new_row = self.table()
            new_row.group_id = values['group_id']
            new_row.perm_name = perm['permission']
            self.request.dbsession.add(new_row)
            
        self.request.dbsession.flush()

    

    def get_values(self, row):
         app_struct = super().get_values(row)
         query = self.query_id()
         app_struct['perm_names'] = [{"permission": p.perm_name} for p in query.all()]
         return app_struct
