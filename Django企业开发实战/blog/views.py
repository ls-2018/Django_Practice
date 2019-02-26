"""
#     request, template_name, context=None, content_type=None, status=None, using=None
content_type：页面编码的类型        默认值是text/html
status  :   状态码，默认200
using   ：  使用哪种引擎解析     ，可以再setting设置，
"""
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from config.models import SideBar
from .models import Post, Category, Tag


class CommonViewMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': self.get_sidebars(),
        })
        context.update(self.get_navs())
        return context

    def get_sidebars(self):
        return SideBar.objects.filter(status=SideBar.STATUS_SHOW)

    def get_navs(self):
        categories = Category.objects.filter(status=Category.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)

        return {
            'navs': nav_categories,
            'categories': normal_categories,
        }


class IndexView(CommonViewMixin, ListView):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        """ 重写queryset，根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """ 重写queryset，根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    model = None  # 指定当前View要使用Model,默认为空
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)  # 和Model二选一，优先级更高，默认为空
    template_name = 'blog/detail.html'  # 模板的名字
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'  # url参数的key

    def get_queryset(self):
        """用来获取queryset,涉及到model以及queryset两个字段"""
        return super(PostDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        """
        获取所有渲染到模板中的所有上下文
        返回一个字典，{k:v}
        """
        return super(PostDetailView, self).get_context_data(**kwargs)

    def get_object(self, queryset=None):
        """根据URL参数，从queryset上获取对应的实例"""
        return super(PostDetailView, self).get_object(queryset)


class PostListView(ListView):
    """因为是列表数据，因此包含分页功能"""
    queryset = Post.latest_posts()
    paginate_by = 1  # 每页的数量为1
    context_object_name = 'post_list'  # 如果不设置此项，在模板中药使用object_list变量
    template_name = 'blog/list.html'
