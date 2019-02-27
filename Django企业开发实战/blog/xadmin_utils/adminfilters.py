from django.contrib import admin
from blog.models import Category
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter


# admin
# class CategoryOwnerFilter(admin.SimpleListFilter):
#     """自定义过滤器只展示当前用户分类"""
#     title = "分类过滤器"
#     parameter_name = 'owner_category'  # 查询时url参数的名字
#
#     def lookups(self, request, model_admin):
#         # 返回要展示的内容和查询用的id，url传的参数
#         return Category.objects.filter(owner=request.user).values_list('id', 'name')
#
#     def queryset(self, request, queryset):
#         # 根据url query 的内容返回列表页数据
#         category_id = self.value()  # ？owner_category=1
#         if category_id:
#             return queryset.filter(category_id=self.value())
#         return queryset

# xadmin    通过对字段名的检测来动态创建对应的过滤器
class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        """确认字段是否需要被当前的过滤器处理"""
        return field.name == 'category'

    def __init__(self, field, request, params, model, admin_view, field_path):
        super().__init__(field, request, params, model, admin_view, field_path)
        # 重新获取lookup_choices 根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)  # 注册，并设置优先权
