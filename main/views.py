from django.shortcuts import render,redirect
from main.models import Category,Blog,About_us,Social_link
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    category=Category.objects.all()
    feature_post=Blog.objects.filter(is_featured=True)
    posted=Blog.objects.filter(is_featured=False,status=1)
    about=About_us.objects.first()
    social=Social_link.objects.first()
    Context={
        'category':category,
        'feature_post':feature_post,
        'posted':posted,
        'about':about,
        'social':social
        }
    return render(request,'core/home-blogs.html',Context)

@login_required
def post_by_category(request,category_id):
    post=Blog.objects.filter(status=1,Category_id=category_id)

    Context={
        'posts':post
    }
    return render(request,'core/post.html',Context)

def slug(request,slug):
    slug=Blog.objects.get(slug=slug)
    category=Category.objects.all()
    Context={
        'slug':slug,
        'category':category
    }   
    return render(request,'core/blog.html',Context)

# def about_us(request):
#     about=About_us.objects.first()

#     return render(request,'core/about-us.html',about)


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = full_name
        user.save()

        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')

    return render(request, 'core/register.html')





def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('login')

        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Password is incorrect')
            return redirect('login')
        else:
            login(request, user) 
            messages.success(request, f'Welcome {user.username}!')
            return redirect('home')  

    return render(request, 'core/login.html')

def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


        





