# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from Django企业开发实战.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
