from django import forms
from dal import autocomplete
from blog.models import Category, Tag, Post
from ckeditor.widgets import CKEditorWidget
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
        widget=autocomplete.ModelSelect2(url='tag-autocomplete'),
        label='标签',
    )
    # content_html = forms.CharField(widget=CKEditorWidget(), label='正文', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'content', 'status', 'is_md')

    class Media:
        js = ('js/post_editor.js',)

    def __init__(self, instance=None, initial=None, **kwargs):
        initial = initial or {}
        if instance:
            if instance.is_md:
                initial['content_html'] = instance.content
            else:
                initial['content_ck'] = instance.content

        super().__init__(instance=instance, initial=initial, **kwargs)
    #
    # def clean(self):
    #     is_md = self.cleaned_data.get('is_md')
    #     if is_md:
    #         content_field_name = 'content_md'
    #     else:
    #         content_field_name = 'content_ck'
    #     content = self.cleaned_data.get(content_field_name)
    #     if not content:
    #         self.add_error(content_field_name, '必填项！')
    #         return
    #     self.cleaned_data['content'] = content
    #     return super().clean()
