#   STATIC_ROOT     
    -   用来配置部署之后的静态资源路径。Django提供了collectionstatic命令来收集所有的京塔资源到STATIC_ROOT配置的目录中，
        这样就可以通过Nginx这样的软件来配置静态资源路径了
    
#   STATIC_URL
    -   用来配置页面上静态资源的起始路径，比如博客列表页中CSS资源拆分之后的地址就是  /static/css/base.css
    -   STATIC_URL = '/static/'
    
#   STATICFILES_DIRS
    -   用来指定静态资源所在的目录。我们访问上面的CSS地址时，Django会去这些目录下查找。
        同时对于上面提到的collectionstatic命令来说，也会去这些目录下查找
        
#   MEDIA_URL
    -   MEDIA_URL = '/media/'        
        
-   通过 THEME 配置，置顶主题文件的整体目录，包括模板和静态资源。

#   模板
    -   使用  {% static 'css/base.css' %}
    -   而不是硬编码，直接写死为   /static/css/base.css
        -   这里的/static/ 是依据 STATIC_URL  得来的
    -   static 并不是Django内置标签，需要在顶部加载改标签     {%  load    static %}
        