# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Django企业开发实战.base_admin import BaseOwnerAdmin
from .models import Comment
import xadmin


@xadmin.sites.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
