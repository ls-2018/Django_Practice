"""Django企业开发实战 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .custom_site import custom_site

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import LinkListView

urlpatterns = [

    # re_path(r"^category/(?P<category_id>\d+)/$", post_detail, {'example': 'nap'}, name='category_list'),
    # 第三个参数定义默认传递到处理函数的参数
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    re_path(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    re_path(r'^links/$', LinkListView.as_view(), name='links'),

    re_path("^search/$", SearchView.as_view(), name='search'),

    path('super_admin/', admin.site.urls),  # 管理用户
    path('admin/', custom_site.urls),  # 管理业务
    # 这两套系统是基于一套逻辑的用户系统，只是我们在url上进行了划分
]
