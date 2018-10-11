from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create(self, *args, **kwargs):
        if len(self.first_name) < 3:
            return 'yo name is too short!'
        else:
        super().create(*args, **kwargs)


