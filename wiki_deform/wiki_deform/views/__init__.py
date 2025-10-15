from wsgiref.validate import validator
import colander

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

pages = {
    '100': dict(uid='100', title='Page 100', body='<em>100</em>'),
    '101': dict(uid='101', title='Page 101', body='<em>101</em>'),
    '102': dict(uid='102', title='Page 102', body='<em>102</em>')
}


class WikiPage(colander.MappingSchema):
    title = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=10, max=15))
    body = colander.SchemaNode(
        colander.String(),
        # widget=deform.widget.RichTextWidget(),
    )


class WikiViews:
    def __init__(self, request):
        self.request = request
        self.buttons = ('submit', 'cancel')

    def form_validator(self, form, value):
        if value['title'] == value['body']:
            exc = colander.Invalid(form, 'Title and Body must differ')
            exc['body'] = 'This is the body error'
            exc['title'] = 'This is the title error'
            raise exc

    @property
    def wiki_form(self):
        schema = WikiPage(validator=self.form_validator)
        # btn_cancel = deform.form.Button(name='cancel', title='Cancel',
        #                                 css_class='btn btn-danger')
        # btn_submit = deform.form.Button(name='submit', title='Submit',
        #                                  css_class='btn btn-success')
        schema = schema.bind(request=self.request)
        return deform.Form(schema, buttons=self.buttons)

    @property
    def reqts(self):
        return self.wiki_form.get_widget_resources()

    @view_config(route_name='wiki_view', renderer='wiki_deform:templates/wiki_view.pt')
    def wiki_view(self):
        return dict(pages=pages.values())

   
    @view_config(route_name='wikipage_add',
                 renderer='wiki_deform:templates/wikipage_addedit.pt')
    def wikipage_add(self):
        form = self.wiki_form.render()
        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Form is valid, make a new identifier and add to list
            last_uid = int(sorted(pages.keys())[-1])
            new_uid = str(last_uid + 1)
            pages[new_uid] = dict(
                uid=new_uid, title=appstruct['title'],
                body=appstruct['body']
            )

            # Now visit new page
            url = self.request.route_url('wikipage_view', uid=new_uid)
            return HTTPFound(url)
        elif 'cancel' in self.request.params:
            url = self.request.route_url('wiki_view')
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='wikipage_view', renderer='wiki_deform:templates/wikipage_view.pt')
    def wikipage_view(self):
        uid = self.request.matchdict['uid']
        page = pages[uid]
        return dict(page=page)

    # @view_config(route_name='wikipage_view',
    #              renderer='wiki_deform:templates/wikipage_addedit.pt')
    # def wikipage_view(self):
    #     uid = self.request.matchdict['uid']
    #     page = pages[uid]
    #     self.buttons = ('edit', 'cancel')
    #     wiki_form = self.wiki_form
    #     return dict(page=page, form=wiki_form.render(page, readonly=True))

    @view_config(route_name='wikipage_edit',
                 renderer='wiki_deform:templates/wikipage_addedit.pt')
    def wikipage_edit(self):
        uid = self.request.matchdict['uid']
        page = pages[uid]

        wiki_form = self.wiki_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=page, form=e.render())

            # Change the content and redirect to the view
            page['title'] = appstruct['title']
            page['body'] = appstruct['body']

            url = self.request.route_url('wikipage_view',
                                         uid=page['uid'])
            return HTTPFound(url)

        elif 'cancel' in self.request.params:
            url = self.request.route_url('wikipage_view', uid=uid)
            return HTTPFound(url)

        form = wiki_form.render(page)

        return dict(page=page, form=form)
