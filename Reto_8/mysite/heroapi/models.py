from django.db import models

class Hero(models.Model):
    # auto_increment_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 60)
    alias = models.CharField(max_length = 60)

    def __str__(self):
        return self.name