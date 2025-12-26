from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Student



def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            image=request.FILES['image']
        )
        return redirect('product_list')
    return render(request, 'firstapp/add_product.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'firstapp/product_list.html', {'products': products})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')
    return render(request, 'firstapp/edit_product.html', {'product': product})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')



from django.shortcuts import render, redirect


def usercreate(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        username   = request.POST.get('username')
        email      = request.POST.get('email')
        password   = request.POST.get('password')
        cpassword  = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('loginpage')

    return render(request, 'firstapp\signup.html')



def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
            return redirect('loginpage')

        user = authenticate(request, username=username, password=password)
    
        if user is None:
            messages.error(request, "Incorrect password")
            return redirect('loginpage')

        login(request, user)
        return redirect('home')

    return render(request, 'firstapp\login.html')


def home(request):
    return render(request, 'firstapp\home.html')

@login_required(login_url='loginpage')
def about(request):
    if request.user.is_authenticated:
        return render(request, 'firstapp/about.html')
    else:
        return render(request, 'firstapp/login.html')


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('loginpage')
    


def home1(request):
    return render(request, 'studentapp/home1.html')


def add_course(request):
    if request.method == 'POST':
        Course.objects.create(
            course_name=request.POST['course_name'],
            course_fee=request.POST['course_fee']
        )
        return redirect('add_course')
    return render(request, 'studentapp/add_course.html')


def add_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            address=request.POST['address'],
            age=request.POST['age'],
            join_date=request.POST['join_date'],
            course_id=request.POST['course']
        )
        return redirect('add_student')

    return render(request, 'studentapp/add_student.html', {'courses': courses})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.name = request.POST['name']
        student.address = request.POST['address']
        student.age = request.POST['age']
        student.join_date = request.POST['join_date']
        student.course_id = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'studentapp/edit.html', {'student': student, 'courses': courses})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        username   = request.POST.get('username')
        email      = request.POST.get('email')
        password   = request.POST.get('password')
        cpassword  = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        messages.success(request, "Account created successfully")
        return redirect('loginpage')

    return render(request, 'studentapp/signup.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home1')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('loginpage')

    return render(request, 'studentapp/login.html')

def logoutuser(request):
    logout(request)
    return redirect('loginpage')








    



