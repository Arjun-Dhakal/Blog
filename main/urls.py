from django.urls import path
from .views import home,post_by_category,slug,log_in,register,log_out


urlpatterns = [
    path('',home, name='home'),
    path('category/<int:category_id>/',post_by_category, name='post'),
    path('slug/<str:slug>/',slug,name='blog'),
    path('register/',register,name='register'),
    path('login/',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    # path('about-us/',about_us,name='about-us')
   
    
    
]
