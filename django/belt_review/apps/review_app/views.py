from django.shortcuts import render, redirect
from django.contrib import messages
from apps.review_app.models import User, Book, Review
import bcrypt


def index(request):
    return render(request, "review_app/index.html")


def dashboard(request):
    if 'id' not in request.session:
        return redirect("/")
    user_data = User.objects.get(id=request.session['id'])
    book_data = Book.objects.all()
    review_data = Review.objects.all()
    master_dict = {
        "pk": user_data,
        "bookkey": book_data,
        "reviewkey": review_data,
    }
    return render(request, "review_app/dashboard.html", master_dict)


def validate_register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
        )
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        request.session['message'] = "registered"
        return redirect("/success")


def validate_login(request):
    request.session['error'] = ""
    try:
        User.objects.get(email=request.POST['login_email'])
    except:
        request.session['error'] += "Incorrect Email"
        return redirect("/")
    user = User.objects.get(email=request.POST['login_email'])
    if user:
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['message'] = "logged in"
            request.session['id'] = user.id
            return redirect("/dashboard")
        else:
            request.session['error'] += "Incorrect Password"
            return redirect("/")


def success(request):
    data = User.objects.get(id=request.session['id'])
    userdict = {
        "datakey": data
    }
    return render(request, "review_app/success.html", userdict)


def add_book(request):
    user_data = User.objects.get(id=request.session['id'])
    datdict = {
        "pk": user_data
    }
    return render(request, "review_app/add.html", datdict)


def validate_add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_book')
    else:
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
        )
        this_user = User.objects.get(id=request.session['id'])
        this_book = Book.objects.get(title=request.POST['title'])
        Review.objects.create(
            reviewer = this_user,
            book = this_book,
            review = request.POST['review'],
            rating = request.POST['rating'],
        )
        return redirect("/add_success")


def add_success(request):
    return render(request, "review_app/add_success.html")


def logoff(request):
    request.session['id'] = None
    return redirect('/')


# def session_handler(request):
#     request.session['user_id'] = request.POST['user_id']
#     return redirect('//wall')


def book(request):
    if 'book_id' not in request.session:
        request.session['book_id'] = request.POST['book_id']
    user_data = User.objects.get(id=request.session['id'])
    book_data = Book.objects.filter(id=request.session['book_id'])
    review_data = Review.objects.all()
    master_dict = {
        "pk": user_data,
        "bookkey": book_data,
        "reviewkey": review_data,
    }
    return render(request, "review_app/book.html", master_dict)


def post_review(request):
    this_user = User.objects.get(id=request.session['id'])
    this_book = Book.objects.get(title=request.POST['title'])
    Review.objects.create(
        reviewer = this_user,
        book = this_book,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )
    return redirect("/book")

def user(request):
    user_data = User.objects.get(id=request.session['id'])
    data = User.objects.filter(id=request.POST['user_id'])
    datuser = {
        "pk": user_data,
        "user": data
    }
    return render(request, "review_app/user.html", datuser)

# def destroy(request):
#     User.objects.filter(id=request.POST['destroyid']).delete()
#     return redirect("/dashboard")