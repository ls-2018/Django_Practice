#   视图函数强烈建议使用request这一参数
#   模范风格
    -   {{ foo }} 正确
    -   {{foo}} 错误
#   Model中的编码规范
    -   字段应该小写+下划线          替代驼峰式命名
    
    -   顺序和空行
        -   字段定义
        -   自定义managers属性
        -   class Meta定义
        -   def __str__  方法
        -   def save 方法
        -   def get_absolute_url方法
        -   其他方法定义
        
    -   choices的定义需要大写
    
    
    
#   Django编码风格
    https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/    