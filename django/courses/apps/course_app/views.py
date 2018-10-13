from django.shortcuts import render, redirect
from apps.course_app.models import Course, CourseForm

def index(request):
    if request.method == "POST":
        return redirect("/users/delete")
    data = Course.objects.all()
    coursedict = {
        "datakey": data
    }
    return render(request, "course_app/index.html", coursedict)

def process(request):
    form = CourseForm(request.POST)
    if form.is_valid():
        form.course_name = request.POST['course_name']
        form.description = request.POST['description']
        form.save()
    return redirect("/courses")

def delete(request):
    data = Course.objects.filter(id=request.POST['destroyid'])
    deletedict = {
        "datakey": data
    }
    return render(request, "course_app/delete.html", deletedict)

def destroy(request):
    Course.objects.filter(id=request.POST['destroyid']).delete()
    return redirect("/courses")