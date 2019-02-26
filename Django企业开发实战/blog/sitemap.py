"""
Sitemap(站点地图)用来描述网站的内容阻止结构，其主要用途是提供给搜索引擎，让他能更好的的索引、收录我们的网站
"""

#   和Feed类似，都是输出文章列表，但是格式和内容均不相同
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 1.0
    protocol = 'https'

    def items(self):
        """返回正常状态的文章"""
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        """返回每篇文章的创建时间"""
        return obj.created_time

    def location(self, obj):
        """返回每篇文章的URL"""
        return reverse('post-detail', args=[obj.pk])

"""
sitemap.xml

url.item.tags需作如下支持，因为Post模型有tag这样一个多对多的关联，所以可以在模型中增加一个属性来输出配置好的tags。紧接着修改blog/models.py中的Post部分。


"""