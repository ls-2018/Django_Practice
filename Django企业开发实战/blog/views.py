"""
#     request, template_name, context=None, content_type=None, status=None, using=None
content_type：页面编码的类型        默认值是text/html
status  :   状态码，默认200
using   ：  使用哪种引擎解析     ，可以再setting设置，
"""
from datetime import date

from django.db.models import Q, F
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.core.cache import cache

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
    queryset = Post.latest_posts()  # 和Model二选一，优先级更高，默认为空
    template_name = "blog/detail.html"  # 模板的名字
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'  # url参数的key

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s' % (uid, self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 1 * 60)  # 1分钟有效

        uv_key = 'uv:%s:%s:%s' % (uid, str(date.today()), self.request.path)
        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key, 1, 24 * 60 * 60)  # 24小时有效

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)

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


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get("keyword", '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get("keyword")
        if not keyword:
            return queryset

        return queryset.filter(Q(title__icontains=keyword) | Q(desc_icontains=keyword))


class AuthorView(IndexView):

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.GET.get("owner_id")
        if not author_id:
            return queryset

        return queryset.filter(owner_id=author_id)
