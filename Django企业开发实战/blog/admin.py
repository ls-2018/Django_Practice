from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .admin_utils.adminforms import PostAdminForm
from .admin_utils.adminInlines import PostInline
from Django企业开发实战.custom_site import custom_site
from Django企业开发实战.base_admin import BaseOwnerAdmin
from blog.admin_utils.adminfilters import CategoryOwnerFilter


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_filter = [CategoryOwnerFilter, ]
    inlines = [PostInline, ]

    list_display = ('name', 'status', 'is_nav', "created_time", 'owner', 'post_count')
    fields = ('name', 'status', 'is_nav', 'owner')

    def __str__(self):
        return self.title

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', "created_time", 'owner')
    fields = ('name', 'status', 'owner')  # 添加或编辑所展示的字段


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = ['title', 'category', 'status', 'created_time', 'username', 'operator']
    list_display_links = []  # 用来配置那些字段可以链接
    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    actions_on_top = True  # 动作相关的配置，是否展示在顶部
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True  # 保存、编辑、编辑并新建按钮是否显示在顶部

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    # 多对多字段是横向展示，还是纵向展示
    filter_horizontal = ('tag',)
    # filter_vertical = ('tag',)  # 纵

    fieldsets = [
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (  # 限定展示的字段；配置展示字段的顺序
                ('title', 'category'),
                'status',
            )
        }),
        ('内容', {
            'description': '内容',
            'fields': (
                'desc',
                'content'
            )
        }),
        ('额外信息', {
            'description': '',
            'classes': ('wide',),  # 给配置的版块加上一些CSS属性，           collapse 和 wide
            'fields': ('tag',)
        })
    ]

    class Meta:
        """通过自定义meta类来往页面上添加想要的Js以及CSS资源"""
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.bundle.js",)

    def __str__(self):
        return self.title

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    def username(self, obj):
        return obj.owner.username

    username.short_description = '作者'
