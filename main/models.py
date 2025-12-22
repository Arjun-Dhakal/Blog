from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    



STATUS_CHOICES=(
    (0,'Draft'),
    (1,'Published')
)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blogs_images/')
    short_description=models.TextField(max_length=300)
    blog_content=models.TextField()
    status=models.IntegerField(choices=STATUS_CHOICES,default=0)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



    
