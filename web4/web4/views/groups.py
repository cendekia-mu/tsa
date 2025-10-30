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

from deform import widget, Form, ValidationFailure
import colander
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..models.auth import Group

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
        widget=widget.HiddenWidget(),
    )

class Views():
    def __init__(self, request):
        self.request = request
        self.table = Group

    @view_config(route_name='group-list', renderer='web4:templates/list_group.pt')
    def view_list(self):
        rows = self.request.dbsession.query(self.table).all()
        return {'rows': rows}

    @view_config(route_name='group-create', renderer='web4:templates/form.pt')
    def view_create(self):
        schema = CreateSchema()
        form = Form(schema, buttons=('save','cancel'))
        if self.request.POST:
            if 'save' in self.request.POST:
                controls = self.request.POST.items()
                try:
                    appstruct = form.validate(controls)
                    self.save(appstruct)
                except ValidationFailure as e:
                    return {'form': e.render()}
                
            return HTTPFound(self.request.route_url('group-list'))
            
        return {'form': form.render()}
    
    def save(self, values, row=None):
        if row is None:
            row = self.table()
        row.group_name = values['group_name']
        row.description = values.get('description', '') # optional karena kemungkinan tidak diisi
        self.request.dbsession.add(row)

    def query_id(self):
        id_ = self.request.matchdict.get('id')
        return self.request.dbsession.query(self.table).filter_by(id=id_)
    
    @view_config(route_name='group-read', renderer='web4:templates/form.pt')
    def view_read(self):
        query = self.query_id()
        if not query.first():
            self.request.session.flash('Group not found!', 'error')
            return HTTPFound(self.request.route_url('group-list'))

        schema = UpdateSchema()
        form = Form(schema, buttons=('cancel','delete'))
        if self.request.POST:
            if 'delete' in self.request.POST:
                return HTTPFound(self.request.route_url('group-delete', id=self.request.matchdict.get('id')))
            
            return HTTPFound(self.request.route_url('group-list'))
        
        appstruct = query.first().__dict__
        return {'form': form.render(appstruct=appstruct)}

    @view_config(route_name='group-update', renderer='web4:templates/form.pt')
    def view_update(self):
        query = self.query_id()
        row = query.first()
        if not row:
            self.request.session.flash('Group not found!', 'error')
            return HTTPFound(self.request.route_url('group-list'))

        schema = UpdateSchema()
        form = Form(schema, buttons=('save', 'cancel'))
        if self.request.POST:
            if 'save' in self.request.POST:
                controls = self.request.POST.items()
                try:
                    appstruct = form.validate(controls)
                    self.save(appstruct, row)
                except ValidationFailure as e:
                    return {'form': e.render()}

            return HTTPFound(self.request.route_url('group-list'))

        appstruct = row.__dict__
        return {'form': form.render(appstruct=appstruct)}

    @view_config(route_name='group-delete', renderer='web4:templates/form.pt')
    def view_delete(self):
        query = self.query_id()
        if not query.first():
            self.request.session.flash('Group not found!', 'error')
            return HTTPFound(self.request.route_url('group-list'))
        
        query.delete()
        self.request.session.flash('Group deleted successfully!')
        return HTTPFound(self.request.route_url('group-list'))

    def form_validator(self):
        pass

