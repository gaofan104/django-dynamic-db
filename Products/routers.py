from .middleware import local_vars


class AuthRouter(object):
    """
    A router to control all database operations on models in the
    django-related application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read django-related models go to 'default'.
        """
        if model._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles']:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write django-related models go to 'default'.
        """
        if model._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles']:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in django-related app are involved.
        """
        if obj1._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles'] or \
           obj2._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles']:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the django-related app only appears in the 'default'
        database.
        """
        if app_label in ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles']:
            return db == 'default'
        return None

class DBRouter(object):
    """
    A router to control all database operations on models in the
    non-Django related application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read non-django related models go to runtime dynamic DB
        The runtime dynamic DB id is extracted from URL parameter and saved in thread local variable by middleware
        """
        return local_vars.database_name

    def db_for_write(self, model, **hints):
        """
        Attempts to write non-django related models go to runtime dynamic DB
        The runtime dynamic DB id is extracted from URL parameter and saved in thread local variable by middleware
        """
        return local_vars.database_name

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        DO NOT migrate non-django related models to default DB
        """
        if db == 'default':
            return False