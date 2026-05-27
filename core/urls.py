from django.urls import path
from .views import dashboard_home, cat_list, blog_list, add_cat, update_cat, delete_cat,add_blog,update_blog,delete_blog,media_list,superuser_login,about_list




urlpatterns = [
    path('',superuser_login,name='superuser_login'),
    path('dash/', dashboard_home, name='dashboard_home'),
    path('categories/', cat_list, name='cat_list'),
    path('blogs/',blog_list,name='blog_list'),
    path('add-category/',add_cat,name='add_cat'),
    path('update/<int:id>/',update_cat,name='update_cat'),
    path('delete/<int:id>/',delete_cat,name='delete_cat'),
    path('add/',add_blog,name='add_blog'),
    path('update_blog/<int:id>/',update_blog,name='update_blog'),
    path('delete_blog/<int:id>/',delete_blog,name='delete_blog'),
    path('media/',media_list,name='media_list'),
    path('about/',about_list,name='about_list')


]
