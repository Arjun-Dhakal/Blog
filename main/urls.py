from django.urls import path
from .views import home,post_by_category,slug,about_us


urlpatterns = [
    path('',home, name='home'),
    path('category/<int:category_id>/',post_by_category, name='post'),
    path('slug/<str:slug>/',slug,name='blog'),
    path('about-us/',about_us,name='about-us')
   
    
    
]
