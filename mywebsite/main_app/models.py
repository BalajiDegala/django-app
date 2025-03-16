# Update in main_app/models.py

from django.db import models
from djongo import models as djongo_models

# PostgreSQL model (using the default Django ORM)
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# MongoDB model (using Djongo)
class UserActivity(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user_id = djongo_models.IntegerField()
    action = djongo_models.CharField(max_length=50)
    page = djongo_models.CharField(max_length=100)
    timestamp = djongo_models.DateTimeField(auto_now_add=True)
    metadata = djongo_models.JSONField(null=True, blank=True)
    
    class Meta:
        # Remove the db_alias attribute
        # We'll use the database router to handle routing instead
        app_label = 'main_app'