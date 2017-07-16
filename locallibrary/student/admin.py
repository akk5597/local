from django.contrib import admin

# Register your models here.
from .models import  Book, BookInstance

#admin.site.register(Book)
#admin.site.register(BookInstance)


# Register the Admin classes for BookInstance using the decorator

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'author','publisher')
     inlines = [BooksInstanceInline]