"""Group-related views for the application.
   1. Table yang digunakan (Group)
        def id(self):
            return sa.Column(sa.Integer(), primary_key=True)

        def group_name(self):
            return sa.Column(sa.Unicode(128), nullable=False, unique=True)

        def description(self):
            return sa.Column(sa.Text())

        def member_count(self): -> tidak dimasukan karena akan dihitung otomatis
            return sa.Column(sa.Integer, nullable=False, default=0)

   2. Relasi dengan tabel lain (Optional Jika Ada)
   3. Buat colander schema
   4. Buat class View
      Function (CRUD):
        - view_list (Menampilkan data dalam bentuk tabel)
        - view_create
        - view_read
        - view_update
        - view_delete
        - form_validator -> Untuk memvalidasi jika field bersifat uniq
        - query_id -> untuk membaca data berdasarkan id 
                      digunakan oleh read update delete
    5. Membuat template yang dibutuhkan pada folder templates/list_groups.pt
    6. Menambahkan route pada file web4/routes.py
        group-list
        group-create
        group-read
        group-update
        group-delete

"""

import logging
import colander
import deform
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models.auth import Group
from web4.views import BaseViews

log = logging.getLogger(__name__)
class CreateSchema(colander.MappingSchema):
    group_name = colander.SchemaNode(
        colander.String(),
        title="Group Name",
        description="Unique name for the group",
        validator = colander.Length(min=3, max=128),
    )
    description = colander.SchemaNode(
        colander.String(),
        title="Description",
        description="Description of the group",
        missing=colander.drop,
    )

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
        self.table = Group 
        self.CreateSchema = CreateSchema  
        self.UpdateSchema = UpdateSchema 
        self.ReadSchema = ReadSchema 
        self.list_route_name = 'group' 

    def form_validator(self, form, value):
        # Custom validation logic can be added here
        exc = colander.Invalid(
            form,
            'Terjadi kesalahan pengisian data'
        )
        id_ = self.request.matchdict.get('id')
        found = self.request.dbsession.query(self.table).filter(
            self.table.group_name == value['group_name'],
            self.table.id != id_ if id_ else True
        ).first()
        if found:
            exc["group_name"] = 'Group name already exists.'
            raise exc


    # @view_config(route_name='group-create', renderer='web4:templates/form.pt')
    # def view_create(self):
    #     return super().view_create()

    # @view_config(route_name='group-read', renderer='web4:templates/form.pt')
    # def view_read(self):
    #     return super().view_read()
    
    # @view_config(route_name='group-update', renderer='web4:templates/form.pt')
    # def view_update(self):
    #     return super().view_update()
    
    # @view_config(route_name='group-list', renderer='web4:templates/list_group.pt')
    # def view_list(self):
    #     return super().view_list()
    
    @view_config(route_name='group-delete')
    def view_delete(self):      
        return super().view_delete()
    