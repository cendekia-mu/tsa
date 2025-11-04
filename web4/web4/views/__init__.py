from web4.models.auth import User
from pyramid.httpexceptions import HTTPFound
import deform
import colander

class CreateSchema(colander.MappingSchema):
    pass

class UpdateSchema(CreateSchema):
    pass

class ReadSchema(UpdateSchema):
    def after_bind(self, node, kw):
        for child in node.children:
            child.widget.readonly = True
            child.missing = colander.drop

class BaseViews(object):
    def __init__(self, request):
        self.request = request
        self.table = User # Default table, can be overridden
        self.CreateSchema = CreateSchema # Default schema, can be overridden
        self.UpdateSchema = UpdateSchema # Default schema, can be overridden
        self.ReadSchema = ReadSchema # Default read schema, can be overridden
        self.list_route_name = 'user-list' # Default list route name, can be overridden
 
    def view_list(self):
        # Logic to fetch all users from the database goes here
        rows = self.table.query().all()
        return {'rows': rows}

    def save(self, values, row=None):
        if not row:
            row = self.table()

        for key, val in values.items():
            if hasattr(row, key):
                setattr(row, key, val)

        self.request.dbsession.add(row)
        self.request.dbsession.flush()
        return row

    def view_create(self):
        form = self.get_form(self.CreateSchema, buttons=('save', 'cancel'))

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

            return HTTPFound(location=self.request.route_url(self.list_route_name))

        rendered_form = form.render()
        return {'form': rendered_form}

    def form_validator(self, form, value):
        pass

    def query_id(self):
        id_ = self.request.matchdict.get('id')
        return self.request.dbsession.query(self.table).filter(self.table.id == id_)
    
    def get_form(self, schema_class, buttons=("cancel", )):
        schema = schema_class(validator=self.form_validator, request=self.request)
        schema = schema.bind(request=self.request)
        form = deform.Form(schema, buttons=buttons)
        return form

    def view_read(self):
        # Logic to fetch user data from the database goes here
        query = self.query_id()
        row = query.first()
        if not row:
            self.request.session.flash('Record not found!')
            return HTTPFound(location=self.request.route_url(self.list_route_name))

        form = self.get_form(self.ReadSchema)
        if self.request.POST:
            return HTTPFound(location=self.request.route_url(self.list_route_name))

        # Pre-fill form with existing user data
        appstruct = self.get_values(row)
        rendered_form = form.render(appstruct)
        return {'form': rendered_form}

    def view_update(self):
        # Logic to fetch user data from the database goes here
        query = self.query_id()
        row = query.first()
        if not row:
            self.request.session.flash('User not found!')
            return HTTPFound(location=self.request.route_url('user'))

        form = self.get_form(self.UpdateSchema, buttons=('save', 'cancel'))
        if self.request.POST:
            if 'save' in self.request.POST:
                controls = self.request.POST.items()
                try:
                    appstruct = form.validate(controls)
                    # Logic to update user in the database goes here
                    user = self.save(appstruct, row)
                    self.request.session.flash('Record updated successfully!')
                except deform.ValidationFailure as e:
                    return {'form': e.render()}

            return HTTPFound(location=self.request.route_url(self.list_route_name))

        # Pre-fill form with existing user data
        appstruct = self.get_values(row)
        rendered_form = form.render(appstruct)
        return {'form': rendered_form}
    
    def get_values(self, row):
        appstruct = dict(row.__dict__)
        # Remove SQLAlchemy internal state
        appstruct.pop('_sa_instance_state', None)
        return appstruct
    

    def view_delete(self):
        # Logic to fetch user data from the database goes here
        query = self.query_id()
        row = query.first()
        if not row:
            self.request.session.flash('Record not found!')
            return HTTPFound(location=self.request.route_url(self.list_route_name))
        if self.request.POST:
            if "delete" in self.request.POST:
                try:
                    query.delete()
                    self.request.session.flash('Record deleted successfully!')
                except Exception as e:
                    self.request.session.flash('Error deleting user: {}'.format(e))

            return HTTPFound(location=self.request.route_url(self.list_route_name))
        
        form = self.get_form(self.ReadSchema, buttons=('delete', 'cancel'))
        app_struct = self.get_values(row)
        form.set_appstruct(app_struct)
        rendered_form = form.render()
        return {'form': rendered_form}