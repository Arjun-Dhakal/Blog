from django.urls import path
from .views import home,post_by_category


urlpatterns = [
    path('',home, name='home'),
    path('category/<int:category_id>/',post_by_category, name='post')
    
    
]
