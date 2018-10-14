from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_Name = models.CharField(max_length=255)
    email = models.EmailField( max_length=255)
    password = models.models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

from django.forms import ModelForm

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


