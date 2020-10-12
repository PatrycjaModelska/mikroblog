from django.contrib import admin
from microblog.models import BlogCategory, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_author',  'created_date', 'publication_date', 'active')
    ordering = ['created_date']
    search_fields = ['id_author', 'title']
    list_filter = ('id_author', 'title', 'created_date', 'publication_date', 'category', 'tag')


admin.site.register(BlogCategory)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
