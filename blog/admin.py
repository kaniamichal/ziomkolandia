from django.contrib import admin
from .models import Post, Comment, Category, ReplyComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(ReplyComment)
