from atexit import register
from re import L
from django.contrib import admin
from .models import Book, BookInstance, Author, Language, Genre
# Register your models here.
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(Author)

# Define the admin class
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    # list_display = ('last_name', 'first_name',
    #                 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', (
    #     'date_of_birth', 'date_of_death')]
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for book using the decorater


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorater


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
