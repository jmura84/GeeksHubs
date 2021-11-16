from django.db import models
from django.conf import settings
from django.utils import timezone

class Api_Author(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    added_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name