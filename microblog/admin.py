from django.contrib import admin
from microblog.models import BlogCategory, Post, Comment
from users.models import Users


class PostAdmin(admin.ModelAdmin):
    list_display = ('id_author', 'title', 'created_date', 'publication_date')
    ordering = ['created_date']
    search_fields = ['id_author', 'title']
    list_filter = ('id_author', 'title', 'created_date', 'publication_date', 'category', 'tag')


admin.site.register(Users)
admin.site.register(BlogCategory)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
