# mywebsite/routers.py

class DatabaseRouter:
    """
    A router to control all database operations on models in the application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user activity models go to mongodb.
        """
        if model._meta.model_name == 'useractivity':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write user activity models go to mongodb.
        """
        if model._meta.model_name == 'useractivity':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'default' database.
        """
        if db == 'mongodb':
            # Don't run migrations for MongoDB
            if model_name == 'useractivity':
                return False
            return False
        return True
