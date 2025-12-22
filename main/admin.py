from django.contrib import admin
from .models import Category, Blog




class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'is_featured',)
    search_fields = ('title', 'author__username',)
    list_editable=('is_featured',)



    
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)