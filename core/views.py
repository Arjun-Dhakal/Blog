from django.shortcuts import render,redirect,get_object_or_404
from core.form import Categoryform
from main.models import Category, Blog, Social_link
from core.form import Categoryform,Blogform,AboutusForm,SociallinkForm
from django.contrib.auth import logout

# Create your views here.
def dashboard_home(request):
    category_count=Category.objects.count()
    blog_count=Blog.objects.count()

    context={
    'category_count':category_count,
    'blog_count':blog_count  
 }

    return render(request, 'dashboard.html',context)

def cat_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)
def add_cat(request):
    if request.method=='POST':
        form=Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    form=Categoryform()
    context={
        'form':form
    }
    
    return render(request,'addcat.html',context)

def update_cat(request,id):
    category=get_object_or_404(Category,id=id)
    if request.method=='POST':
        form=Categoryform(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    form=Categoryform(instance=category)
    context={
        'form':form
    }
    return render(request,'addcat.html',context)

def delete_cat(request,id):
    category=get_object_or_404(Category,id=id)
    category.delete()
    return redirect('cat_list')




def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = Blogform()

    return render(request, 'addblog.html', {'form': form})

def update_blog(request, id):
    blog=get_object_or_404(Blog,id=id)
    if request.method=='POST':
        form=Blogform(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    form=Blogform(instance=blog)
    return render(request,'addblog.html',{'form':form})

def delete_blog(request,id):
    blog=get_object_or_404(Blog,id=id)
    blog.delete()
    return redirect('blog_list')

def media_list(request):
    media = Social_link.objects.last()
    return render(request, 'media.html', {'media': media})

from django.contrib.auth import authenticate, login
from django.contrib import messages

def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard_home')  # change to your url name
            else:
                messages.error(request, "You are not a superuser.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('superuser_login')


  
