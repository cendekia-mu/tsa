# Wiki
## Table
### Users

```
id,
name, 
role 
```

### Pages

```
id, 
name, 
data ,
creator_id| ForeignKey(User, [id])
```

## Views

```
home_view  beranda
add_view   tambah
edit_view  koreksi
view_view  lihat
login_view
logout_view

```

## Templates
* Home Template
* Viewing Lihat
* Add dan Edit

## Security
* Authentiction (Login)
* Authorization (Hak Akses)
* 

## Role
```
basic
editor
```

## Route
```
/
/Page
/Page/edit
/Page/add
/login
/logout
```

# Langkah Kerja
## Memulai / Install/ Setup Development
1. Membuat Virtual environment
2. Activasi Environement
3. Install CookieCutter
4. Membuat Project
   ```
   name=wiki
   template=jinja2
   db=sqlalchemy
   ```
5. Masuk ke folder project
6. Install Aplikasi
7. Inistial Database (Setup Database)
8. Inisial data
9.  test Aplikasi
10. Jalankan Aplikasi

## Menambahkan Module
