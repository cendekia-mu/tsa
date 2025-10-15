# Create web4 Application

- Create Application type chameleon with sqlalchemy
  
  ```cookiecutter pyramid-cookiecutter-starter```

- Install aplikasi
  
  ```pip install -e ".[testing]"```



# Configurasi Database

- Add Database configuration to ```development.ini```

  ```
  [app:main]
  ...
  sqlalchemy.url = postgresql://user:pass@server:port/db

  ...

  [alembic]
  sqlalchemy.url = postgresql://user:pass@server:port/db
  ```
- Init Alembic
  
  ```alembic -c development.ini revision --autogenerate -m "init"```

- Run Alembic 
  
  ```alembic -c development.ini upgrade head```
  * Ini akan membuat tabel ```models``` dalam database

- Perbaiki ```models/__init__.py```
  ```
  from .meta import Base

  DBSession = sessionmaker(class_=Session)
  zope.sqlalchemy.register(DBSession)

  ...

  def includeme(config):
      ...
      DBSession.configure(bind=dbengine)

  ```

- Buat file ```auth.py``` dalam models

  Isi dengan Script dari https://ziggurat-foundations.readthedocs.io/en/latest/configuration.html
  
  ```
  # ... your DBSession and base gets created in your favourite framework ...
  
  ```
  * Perbaiki hal-hal yang kurang 
  
- Jalankan kembali Init Alembic
  
  ```alembic -c development.ini revision --autogenerate -m "init"```

- Run Alembic 
  
    ```alembic -c development.ini upgrade head```
  * Ini akan membuat tabel ```users, groups ``` dan yg lainnya dalam database
  
- Tambahkan script berikut ini pada file ```scripts/initialize_db```
  
  ```
  def setup_models(dbsession):
      
      ...

      group = models.auth.Group(group_name='admins', description='Administrators')
      dbsession.add(group)

      admin = models.auth.User(user_name= 'admin', email='admin')
      dbsession.add(admin)
      UserService.set_password(admin, 'admin')
      dbsession.flush()
      user_group = models.auth.UserGroup(user_id=admin.id, group_id=group.id)
      dbsession.add(user_group)
  ```

- Jalankan ```initialize_web4_db development.ini```

  Ini akan menginsert data kedalam tabel ```models, users, groups, users_groups```

# Menambahkan login dan logout
- Tambahkan konfigurasi pada ```development.ini```

  ```
  pyramid.includes =
      ...
      pyramid_tm
      ziggurat_foundations.ext.pyramid.sign_in

  ziggurat_foundations.model_locations.User = web4.models:User
  # name of the POST key that will be used to supply user name
  ziggurat_foundations.sign_in.username_key = login

  # name of the POST key that will be used to supply user password
  ziggurat_foundations.sign_in.password_key = password

  # name of the POST key that will be used to provide additional value that can be used to redirect
  # user back to area that required authentication/authorization)
  ziggurat_foundations.sign_in.came_from_key = came_from

  # If you do not use a global DBSession variable, and you bundle DBSession insde the request
  # you need to tell Ziggurat its naming convention, do this by providing a function that
  # returns the correct request variable
  ziggurat_foundations.session_provider_callable = web4.models:get_session_callable
  ```

- Tambahkan script berikut ini pada ```models/__init__.py```

  ```
  def get_session_callable(request):
      return request.dbsession
  ```

- Buat Template ```templates/login.pt```

  ```
  <form action="{{request.route_url('ziggurat.routes.sign_in')}}" method="post">
      <!-- "came_from", "password" and "login" can all be overwritten -->
      <input type="hidden" value="OPTIONAL" name="came_from" id="came_from">
      <!-- in the example above we changed the value of "login" to "username" -->
      <input type="text" value="" name="login" <!-- change to name="username" if required --> >
      <input type="password" value="" name="password">
      <input type="submit" value="Sign In" name="submit" id="submit">
  </form>
  ```
- Tambahkan Route ```routes.py```

  ```
  config.add_route('login', '/login')
  ```

- Buat View ```views/login.py```

  ```
  from pyramid.security import NO_PERMISSION_REQUIRED
  from ziggurat_foundations.ext.pyramid.sign_in import ZigguratSignInSuccess
  from ziggurat_foundations.ext.pyramid.sign_in import ZigguratSignInBadAuth
  from ziggurat_foundations.ext.pyramid.sign_in import ZigguratSignOut
  ZigguratSignInSuccess context view example

  
  @view_config(route_name='login', renderer='web4:templates/login.pt')
  def login(request):
      return {"came_from": request.params.get("came_from", "/")}


  @view_config(context=ZigguratSignInSuccess, permission=NO_PERMISSION_REQUIRED)
  def sign_in(request):
      # get the user
      user = request.context.user
      # actions performed on sucessful logon, flash message/new csrf token
      # user status validation etc.
      if request.context.came_from != '/':
          return HTTPFound(location=request.context.came_from,
                          headers=request.context.headers)
      else:
          return HTTPFound(location=request.route_url('some_route'),
                          headers=request.context.headers)
  
  @view_config(context=ZigguratSignInBadAuth, permission=NO_PERMISSION_REQUIRED)
  def bad_auth(request):
      # The user is here if they have failed login, this example
      # would return the user back to "/" (site root)
      return HTTPFound(location=request.route_url('/'),
                      headers=request.context.headers)
      # This view would return the user back to a custom view
      return HTTPFound(location=request.route_url('declined_view'),
                  headers=request.context.headers)
  
  @view_config(context=ZigguratSignOut, permission=NO_PERMISSION_REQUIRED)
  def sign_out(request):
      return HTTPFound(location=request.route_url('/'),
                      headers=request.context.headers)
  ```

- Tambahkan script berikut ini pada development.ini

  ```
  session.secret = sUpersecret
  ```

- Berikutnya mengubah ```main.py```

  ```
  from ziggurat_foundations.models import groupfinder

  def main(global_config, **settings):

      # Set the session secret as per out ini file
      session_factory = SignedCookieSessionFactory(
          settings['session.secret'],
      )

      authn_policy = AuthTktAuthenticationPolicy(settings['session.secret'],
          callback=groupfinder)
      authz_policy = ACLAuthorizationPolicy()

      # Tie it all together
      config = Configurator(settings=settings,
                root_factory='yourapp.models.RootFactory',
                            authentication_policy=authn_policy,
                            authorization_policy=authz_policy)

      ...
  ```

- Terakhir Menambahkan configurasi pada ```development.ini```
  
  ```
  pyramid.includes = pyramid_tm
                    ziggurat_foundations.ext.pyramid.get_user
  ```

- Jalankan Aplikasi

  ```
  pserve development.ini
  ```
- Test URL http://localhost:6543/login