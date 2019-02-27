from django.contrib import admin
from blog.models import Category


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
