from django.utils import timezone
from django.db import models


# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(null=False, max_length=30)
    username = models.CharField(unique=True, null=False, max_length=15)
    age = models.IntegerField()
    bio = models.TextField()
    password = models.CharField(null=False, max_length=60)
    salt = models.TextField(null=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user_details"
