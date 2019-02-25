from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'blog'
    site_title = 'Django企业开发实战'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
