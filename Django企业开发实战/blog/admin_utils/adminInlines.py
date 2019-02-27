from xadmin.layout import Row, Fieldset, Container
from blog.models import Post


class PostInline:  # StackedInline 样式不同
    """例子：在分类页面直接编辑文章"""
    form_layout = [
        Container(
            Row('title', 'desc'),
        )
    ]
    extra = 1  # 控制额外多几个
    model = Post
