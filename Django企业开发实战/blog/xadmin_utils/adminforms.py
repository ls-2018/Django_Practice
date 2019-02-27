from django import forms
from dal import autocomplete
from blog.models import Category, Tag, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)  # 摘要
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )
    content_ck = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=False)  # 页面展示
    content_md = forms.CharField(widget=forms.Textarea(), label='正文', required=False)  # 页面展示，通过post_editor.js实现哪一个显示
    # 页面加载时，判断"markdown语法"复选框是否选中；如果选中，则展示Markdown编辑器；如果没有选中，则展示django-ckeditor编辑器。
    # 另外一部分是 该复选框点击事件的监听，点击后，根据是否选中进行编辑器切换
    content = forms.CharField(widget=forms.HiddenInput(), required=False)  # 默认隐藏，用来接受最终的编辑内容

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'is_md', 'status', 'content', 'content_md', 'content_ck')

    def __init__(self, instance=None, initial=None, **kwargs):
        initial = initial or {}
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content  # 各字段初始值，instance是当前文章的实例
            else:
                initial['content_ck'] = instance.content

        super().__init__(instance=instance, initial=initial, **kwargs)

    def clean(self):
        """判断是否使用了markdown语法"""
        is_md = self.cleaned_data.get('is_md')
        if is_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name, '必填项！')
            return
        self.cleaned_data['content'] = content
        return super().clean()

    class Media:
        js = ('js/post_editor.js',)
