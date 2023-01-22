# django-app-in-python

## Checking current version
```
$ python -m django --version

4.1.5
```

## Creating a new project
```
$ django-admin startproject mysite

mysite/
    manage.py
    mysite/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

## Executing a development server
```
$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 15, 2023 - 18:40:28
Django version 4.1.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Changing the port
```
$ python manage.py runserver 8080

Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 15, 2023 - 18:44:14
Django version 4.1.5, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.
```

### Changing the server IP
```
$ python manage.py runserver 0.0.0.0:8080

Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 15, 2023 - 18:44:37
Django version 4.1.5, using settings 'mysite.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CTRL-BREAK.
```

## Creating the Polls app
```
$ python manage.py startapp polls

polls/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

## Write your first view

### Edit a file polls/views.py
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Create a file polls/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Edit a file mysite/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## Executing a migration command
```
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## Creating a superuser for admin
```
$ python manage.py createsuperuser

Username (leave blank to use '<username>'): admin
Email address: admin@server.com
Password: Qwerty123*
Password (again): Qwerty123*
```

## Creating the Newsletters app
```
$ python manage.py startapp newsletters

polls/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

### Creating a first model
#### Edit models.py and add Registered class
```
class Registered(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.email
```
#### Execute migration changes to database
```
$ python manage.py makemigrations
newsletters\migrations\0001_initial.py
   - Create model Registered

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, newsletters, sessions
Running migrations:
  Applying newsletters.0001_initial... OK
```

### Creating data for new model using shell
```
$ python manage.py shell

>>> from newsletters.models import Registered
>>> people = Registered.objects.all()
>>> people
<QuerySet []>

>>> person1 = Registered.objects.create(name='Alexander Zuluaga', email='dazulu4@gmail.com')
>>> person1
<Registered: dazulu4@gmail.com>
>>> people
<QuerySet [<Registered: dazulu4@gmail.com>]>
```

#### Edit admin.py to add a Registered model
```
from .models import Registered
admin.site.register(Registered)
```
#### Launch server and validate data for model
```
$ python manage.py runserver
```
Open application in admin module [http://localhost:8000/admin](http://localhost:8000/admin) and validate new Registered data model.

### Customize model in admin module

#### Edit admin.py to add a registered admin class
```
from .models import Registered

class RegisteredAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'timestamp']
    # list_display_links = ['email']
    list_filter = ['timestamp']
    list_editable = ['name']
    search_fields = ['email', 'name']
    class Meta:
        model = Registered

admin.site.register(Registered, RegisteredAdmin)
```

### Generate static files for project
```
$ python manage.py collectstatic

130 static files copied to '\\django-app-in-python\static'.
```