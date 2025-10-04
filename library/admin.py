from django.contrib import admin
from .models import Author, Category, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_categories', 'published')

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    get_categories.short_description = 'Categories'

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)