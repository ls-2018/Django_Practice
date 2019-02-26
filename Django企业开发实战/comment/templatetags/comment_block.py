from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()


@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target)
    }


"""
因为是自定义的标签，因此需要在模板的最上面（但是需要在extends下面）增加{% load comment_block %}
用来加载我们自定义的标签文件

然后在需要的展示评论的地方增加{% comment_block request.path %} 
这里的request全局变量
"""
