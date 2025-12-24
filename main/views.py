from django.shortcuts import render
from main.models import Category,Blog


# Create your views here.
def home(request):
    category=Category.objects.all()
    feature_post=Blog.objects.filter(is_featured=True)
    posted=Blog.objects.filter(is_featured=False,status=1)
    Context={
        'category':category,
        'feature_post':feature_post,
        'posted':posted
        }
    return render(request,'core/home-blogs.html',Context)

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

def about_us(request):

    return render(request,'core/about-us.html')



