from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'status')
    search_fields = ('title', 'author')
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')
    mark_as_published.short_description = "선택된 도서를 게시된 것으로 표시"

admin.site.register(Book, BookAdmin)

# Register your models here.
