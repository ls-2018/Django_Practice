"""Django企业开发实战 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

from django.urls import path, re_path, include

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from .autocomplete import CategoryAutocomplete, TagAutocomplete
import xadmin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from blog.apis import PostViewSet

router = DefaultRouter()
router.register(r"post", PostViewSet, base_name='post')

urlpatterns = [

                  # 第三个参数定义默认传递到处理函数的参数
                  # path("", IndexView.as_view(), name="index"),
                  # re_path(r"category/(?P<category_id>\d+)/", CategoryView.as_view(), name="category-list"),
                  # re_path(r"tag/(?P<tag_id>\d+)/", TagView.as_view(), name="tag-list"),
                  # re_path(r"post/(?P<post_id>\d+).html", PostDetailView.as_view(), name="post-detail"),
                  # re_path(r"author/(?P<owner_id>\d+)/", AuthorView.as_view(), name="author"),
                  #
                  # path("links/", LinkListView.as_view(), name="links"),
                  # path("comment/", CommentView.as_view(), name="comment"),
                  #
                  # path("search/", SearchView.as_view(), name="search"),
                  #
                  # path("admin/", xadmin.site.urls),  # 管理用户
                  #
                  # #   搜索接口
                  # re_path(r"category-autocomplete/$", CategoryAutocomplete.as_view(), name='category-autocomplete'),
                  # re_path(r"tag-autocomplete/$", TagAutocomplete.as_view(), name='tag-autocomplete'),
                  #
                  # # 配置RSS和SITEMAP的路由
                  # re_path(r"rss|feed/$", LatestPostFeed(), name="rss"),
                  # re_path(r"sitemap\.xml$", sitemap_views.sitemap, {"sitemaps": {"posts": PostSitemap}}),
                  #
                  # path("ckeditor/", include('ckeditor_uploader.urls')),  # 文件上传

                  # restframeful 插件
                  # re_path('api/post/$',post_list,name='post-list'),
                  # re_path('api/post', PostList.as_view(), name='post-list')
                  # re_path("api/", include(router.urls, namespace="api")),
                  re_path("api/", include(router.urls, )),

                  re_path('api/docs/$', include_docs_urls(title='Django企业开发实战 apis')),
                  # 通过简单配置就可以得到接口文档，  视图类的   docstring
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 文件浏览
