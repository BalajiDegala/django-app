# mywebsite/routers.py

class DatabaseRouter:
    """
    A router to control all database operations on models in the application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user activity models go to mongodb.
        """
        # Check by model name
        if model.__name__ == 'UserActivity':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write user activity models go to mongodb.
        """
        # Check by model name
        if model.__name__ == 'UserActivity':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is involved.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the UserActivity model doesn't have migrations in MongoDB.
        """
        if db == 'mongodb':
            # For MongoDB, only allow migrations for UserActivity model
            if model_name == 'useractivity':
                return False
            return False
        else:
            # For default DB, don't migrate UserActivity model
            if model_name == 'useractivity':
                return False
        return True