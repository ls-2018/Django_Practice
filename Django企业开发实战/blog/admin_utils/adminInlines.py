from django.contrib import admin
from blog.models import Post


class PostInline(admin.TabularInline):  # StackedInline 样式不同
    """例子：在分类页面直接编辑文章"""
    fields = ['title', 'owner', 'desc', ]
    extra = 0  # 控制额外多几个
    model = Post
