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

    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title_length"] = "Title cannot be less than two characters!"
        if len(postData['author']) < 2:
            errors["author_length"] = "Author Name cannot be less than two characters!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(('password'), max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name="given_reviews")
    book = models.ForeignKey(Book, related_name="received_reviews")
    review = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)    
    objects = BlogManager()

