# django-dynamic-db
A Django sample project to support dynamic DB. 
By providing the url parameter with the specific database id set in django configuration file (settings.py), you are now able to route to
specific DB during runtime.

## Versions
* Django 1.11
* Python 3.x

## Strategies:
1. catch URL parameter in middleware, then set to thread local variable (assume each http request is processed within a single thread)
2. use django routers to first route django builtin app (eg. Auth, Admin) to master DB (default)
3. route custom app to specific DB provided in the URL parameter (thread local variable)
4. however, admin url does not allow regular expression to catch URL parameter as admin views does not take additional URL parameter
in key word arguments (eg. ```url(r'^admin/(?P<db_id>[a-zA-Z0-9]+)', admin.site.urls)``` throws error). We need to use another URL
parameter syntax (ie. `http://127.0.0.1:8000/admin/?db_id=db1`), and in url patterns, we just set `url(r'^admin/', admin.site.urls)`

## Comments:
These ideas come from different people and I could not find their names. Thanks to these awesome people.
