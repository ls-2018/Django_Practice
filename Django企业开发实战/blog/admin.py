from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = "分类过滤器"
    parameter_name = 'owner_category'  # 查询时url参数的名字

    def lookups(self, request, model_admin):
        # 返回要展示的内容和查询用的id，url传的参数
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        # 根据url query 的内容返回列表页数据
        category_id = self.value()  # ？owner_category=1
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = [CategoryOwnerFilter, ]
    list_display = ('name', 'status', 'is_nav', "created_time", 'owner', 'post_count')
    fields = ('name', 'status', 'is_nav', 'owner')

    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        # admin保存前做一些操作
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', "created_time", 'owner')
    fields = ('name', 'status', 'owner')  # 添加或编辑所展示的字段


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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
    # filter_horizontal = ('tag',)
    filter_vertical = ('tag',)  # 纵

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

    def __str__(self):
        return self.title

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    def username(self, obj):
        return obj.owner.username

    username.short_description = '作者'

    def save_model(self, request, obj, form, change):
        # admin保存前做一些操作
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
