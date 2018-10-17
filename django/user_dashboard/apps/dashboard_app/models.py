from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name_length"] = "First Name cannot be less than two characters!"
        if not postData['first_name'].isalpha():
            errors["first_name_alpha"] = "First Name cannot contain numbers!"
        if len(postData['last_name']) < 2:
            errors["last_name_length"] = "Last Name cannot be less than two characters!"
        if not postData['last_name'].isalpha():
            errors["last_name_alpha"] = "Last Name cannot contain numbers!"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_regex'] = "Invalid Email!"
        if User.objects.filter(email=postData['email']):
            errors['email_taken'] = "Email already taken."
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must be 8+ characters!"
        if postData['password'] != postData['confirm_password']:
            errors['password_confirmation'] = "Passwords do not match!"
        return errors

    def update_validator(self, postData):
        errors = {}
        if len(postData['edit1']) < 2:
            errors["first_name_length"] = "First Name cannot be less than two characters!"
        if not postData['edit1'].isalpha():
            errors["first_name_alpha"] = "First Name cannot contain numbers!"
        if len(postData['edit2']) < 2:
            errors["last_name_length"] = "Last Name cannot be less than two characters!"
        if not postData['edit2'].isalpha():
            errors["last_name_alpha"] = "Last Name cannot contain numbers!"
        if len(postData['edit3']) < 1:
            errors["email"] = "Email cannot be empty!"
        if not EMAIL_REGEX.match(postData['edit3']):
            errors['email_regex'] = "Invalid Email!"
        return errors

    def update_validator_2(self, postData):
        errors = {}
        if len(postData['edit4']) < 8:
            errors['password_length'] = "Password must be 8+ characters!"
        if postData['edit4'] != postData['edit5']:
            errors['password_confirmation'] = "Passwords do not match!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(('password'), max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()
    user_level = models.PositiveSmallIntegerField(default=1)


class Message(models.Model):
    poster = models.ForeignKey(User, related_name="messages")
    recipient = models.ForeignKey(User, related_name="received_messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    commenter = models.ForeignKey(User, related_name="comments")
    commented = models.ForeignKey(Message, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
