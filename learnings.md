# Lession 1
- ### install venv
    - sudo pip3 install virtualenv on top root level of the project 
- create venv virtualenv venv -p python3
-  activate virtual venv source venv/bin/activate
- you cna deactiavte using "deactivate"
- for installing django and creating a project Take refrerance of this [Artical](https://medium.com/@diwassharma/starting-a-python-django-project-on-mac-os-x-c089165cf010)
- Add HomePage function and add that view to urls.py (ccec03ee998cdcd7d618de41ce87f9e95d2eeab8)

# Lession 2
- To make project modular we need to add the multiple app to the project that every app consist of it own file of views 
```
python manage.py startapp <appname>
```
- add urls.py file to it. import the urls in in urls.py of root app with keyword includes

# Lession 3 (Migration)
- create a Model that is class that speficy the type values you want to store.
- you will be creating the model in models.py. this model is used to create the tables in your database
- no make migration. inorder to migrate the models you have created 

```
for makeing m migration file:
python manage.py makemigrations

for migrating 
python manage.py migrate

```

# Lession 4 (Django ORM)
- Django ORM is inbuilt ORM that interact wth the Database 

# Lession 5 (Admin)
- In order to work with the rest framework add rest_framework to the installed apps


