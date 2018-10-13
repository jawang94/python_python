from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

from django.forms import ModelForm

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description']
        



