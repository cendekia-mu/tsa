# Web4

1. Melatih membuat model
2. Melatih Membuat view

## Models 
### Authentication & Authorization (auth.py)
1. Users
2. Groups
3. UserGroups
4. UserPermission
5. GroupPermission
6. Resource
7. UserResource
8. GroupResource

## Views

1. Form/View Login
2. Form/View Logout
3. Form Users
  
     * List User
     * Add User
     * Edit User
     * Delete User

4. Form/View Groups
     * List User
     * Add User
     * Edit User
     * Delete User
  
# Route
1. home, /home
2. login, /login
3. logout, /logout
4. users, /users
   1. users-add, /users/add
   2. users-edit, /users/{id}/edit
   3. users-view, /users/{id}/view
   4. users-delete, /users/{id}/delete
5. groups 
   1. groups-add, /groups/add
   2. groups-edit, /groups/{id}/edit
   3. groups-view, /groups/{id}/view
   4. groups-delete, /groups/{id}/delete
6. resources, /resources
   1. resources-add, /resources/add
   2. resources-edit, /resources/{id}/edit
   3. resources-view, /resources/{id}/view
   4. resources-delete, /resources/{id}/delete
   
7. users-groups, /users/groups
   1. users-groups-add, /users/groups/add
   2.  users-groups-edit, /users/groups/{id}/edit
   3.  users-groups-view, /users/groups/{id}/view
   4.  users-groups-delete, /users/groups/{id}/delete

8. users-resources, /users/resources
   1. users-resources-add, /users/resources/add
   2. users-resources-edit, /users/resources/{id}/edit
   3. users-resources-view, /users/resources/{id}/view
   4. users-resources-delete, /users/resources/{id}/delete
    
9. groups-resources, /groups/resources
    1.  groups-resources-add, /groups/resources/add
    2.  groups-resources-edit, /groups/resources/{id}/edit
    3.  groups-resources-view, /groups/resources/{id}/view
    4.  groups-resources-delete, /groups/resources/{id}/delete
   
# Referensi:

https://docs.pylonsproject.org/

https://docs.pylonsproject.org/projects/deform/en/latest/index.html
