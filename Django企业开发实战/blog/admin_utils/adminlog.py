from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model


# 如何记录对象的变更日志
class LogRecord(admin.ModelAdmin):
    """
    代码位置：D:\Python35\Lib\site-packages\django\contrib\admin\options.py

    """

    def log_addition(self, request, object, message):
        """记录新增日志"""
        from django.contrib.admin.models import LogEntry, ADDITION
        return LogEntry.objects.log_action(
            user_id=request.user.pk,  # 用户id
            content_type_id=get_content_type_for_model(object).pk,  # 保存内容的类型
            object_id=object.pk,  # 实际变更记录id
            object_repr=str(object),  # 实例的展示名称
            action_flag=ADDITION,
            change_message=message,
        )

    def log_change(self, request, object, message):
        """记录变更日志"""
        from django.contrib.admin.models import LogEntry, CHANGE
        return LogEntry.objects.log_action(
            user_id=request.user.pk,  # 用户id
            content_type_id=get_content_type_for_model(object).pk,  # 保存内容的类型
            object_id=object.pk,  # 实际变更记录id
            object_repr=str(object),  # 实例的展示名称
            action_flag=CHANGE,
            change_message=message,
        )

    def log_deletion(self, request, object, object_repr):
        """记录删除日志"""
        from django.contrib.admin.models import LogEntry, DELETION
        return LogEntry.objects.log_action(
            user_id=request.user.pk,  # 用户id
            content_type_id=get_content_type_for_model(object).pk,  # 保存内容的类型
            object_id=object.pk,  # 实际变更记录id
            object_repr=object_repr,  # 实例的展示名称
            action_flag=DELETION,
        )


# 如何查询记录的变更
class LookLog:
    from django.contrib.admin.models import LogEntry, CHANGE
    from blog.models import Post
    post = Post.objects.get(id=1)
    log_entries = LogEntry.objects.filter(
        content_type_id=get_content_type_for_model(post).pk,        # 获取表在content_type中的id
        object_id=post.id
    )
