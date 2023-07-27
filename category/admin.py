from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} #field slug kế thừa từ category_name
    list_display = ('category_name', 'slug')    # hiển thị các fieldS

admin.site.register(Category, CategoryAdmin)