from django.urls import path
from .views import home,post_by_category,slug,log_in,register


urlpatterns = [
    path('',home, name='home'),
    path('category/<int:category_id>/',post_by_category, name='post'),
    path('slug/<str:slug>/',slug,name='blog'),
    path('register/',register,name='register'),
    path('login/',log_in,name='login')
    # path('about-us/',about_us,name='about-us')
   
    
    
]
