from django.db import models
from django.conf import settings
from django.utils import timezone

AUTH_USER_MODEL = 'api_bookstore.MyUser'

'''
The above variable is used to override / substitute the default User model that can give issues like ImproperlyConfigured: 
https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

Error example:
Exception: Could not resolve URL for hyperlinked relationship using view  name "user-detail". 
You may have failed to include the related model in your API, or incorrectly configured the `lookup_field`
attribute on this field.
'''

class Api_Author(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Api_Book(models.Model):
    # id = models.AutoField(primary_key=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    author_id = models.ForeignKey(Api_Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title