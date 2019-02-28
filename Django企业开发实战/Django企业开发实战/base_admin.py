# coding:utf-8
from __future__ import unicode_literals

import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin:
    """
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner',)

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()


class GlobalSetting(CommAdminView):
    site_title = 'Typeidea管理后台'
    site_footer = 'power by the5fire.com'


xadmin.site.register(CommAdminView, GlobalSetting)
