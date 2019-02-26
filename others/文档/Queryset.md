#   QuerySet接口

#   支持链式调用的接口
    -   all
    -   filter
        -   contains                包含
        -   icontains               忽略大小写
        -   exact                   精确匹配
        -   iexact                  忽略大小写
        -   in                      
        -   gt                      大于
        -   gte                     大于等于
        -   lt                      小于
        -   lte                     小于等于
        -   startswith              类似contains  ，   只是会产生LIKE   '关键词%'这样的SQL
        -   istartwwith             忽略大小写
        -   endswith
        -   iendswith
        -   range                   create_time__range=('2018-05-01','2019-01-01')
          
        
    -   exclude     同filter相反的逻辑
    -   reverse     把queryset中的结果倒序排列
    -   distinct    去重
    -   none        返回空的queryset
    -   values          返回的结果包含dict的queryset
    -   values_list     返回的结果按查询字段的顺序的元组的queryset
    
#   不支持链式调用的接口
    -   get             一般返回一个实例，否则抛出  DoesNotExist异常
    -   create          
    -   get_or_create   
    -   update_or_create
    -   count
    -   latest          用于返回最新的一条记录，但需要在Meta中定义get_latest_by=<用来排序的字段>
    -   earlist         同上，返回最早的一条数据
    -   first           获取queryset中记录第一条
    -   last            同上，获取最后一条
    -   exists          返回True \ False  ,在数据库层面执行  select （1） as "a" from table_name limit 1 的查询，如果只是需要
                        判断queryset是否有数据，用这个接口是最合适的方式，不要用count或者len这样的操作。
                        相反，如果下文会用到queryset中的数据，可以考虑使用len(queryset)的方式来做判断，这样可以减少一次DB查询请求
    -   bulk_create     同create,用于批量创建创建记录
    -   in_bulk         批量查询，接受两个参数id_list,field_name
                        .objects.in_bulk([1,2,3])       ------>     {1:<实例1>,2:<实例2>,3:<实例3>}                    
    -   update          用来根据条件批量更新记录
    -   delete

    
    
    
    
#   高级接口
    -   defer           
        把不需要的字段做延迟加载
        posts = Post.objects.all().defer("content")
        for post in posts:      # 此时会执行数据库查询
            print(post.content)  # 此时会执行数据库查询，获取到content
        
        当不想加载某个过大的字段时（如text类型的字段，会使用defer），但上面的演示会产生N+1的查询问题，在实际使用时千万要注意。
                在外键查询时也会产生N+1的问题
            
      
    -   only            
        与defer相反，只加载某字段，之后读取任何属性都会产生查询
    
    
    -   select_related  ·
        用来解决外键产生的N+1的问题的方案。

        posts = Post.objects.all().defer("content")
            for post in posts:      # 产生数据库查询
                print(post.owner)   # 产生额外的数据库查询,关联表 owner
        
        posts = Post.objects.all().select_related('category')
            for post in posts:      # 产生数据库查询，category也会一次性查询出来
                print(post.category)    #   相当于连表操作
        
        当然这个接口，只能用来解决一对多的关联关系。
    
    -   prefetch_related    
        用来多对多字段的产生的N+1方案
        posts = Post.object.all().prefetch_related('tag')
        for post in posts:  # 产生两条查询语句，分别是post和tag
            print(post.tag.all())
        
        
#   进阶查询
    -   F
        用来执行数据库层面的计算，从而避免出现竞争状态
        object.all().update(pv=F('pv')+1)
        在数据库层面执行原子操作
    
    -   Q
        用来解决OR查询操作的
        .filter(Q(id=1) | Q(id=2))
        .filter(Q(id=1) & Q(id=2))   
         
        class Q(tree.Node):  
            # Connection types  
            AND = 'AND'  
            OR = 'OR'  
            default = AND  
          
            def __init__(self, *args, **kwargs):  
                super(Q, self).__init__(children=list(args) + kwargs.items())  
          
            def _combine(self, other, conn):  
                if not isinstance(other, Q):  
                    raise TypeError(other)  
                obj = type(self)()  
                obj.add(self, conn)  
                obj.add(other, conn)  
                return obj  
          
            def __or__(self, other):  
                return self._combine(other, self.OR)  
          
            def __and__(self, other):  
                return self._combine(other, self.AND)  
          
            def __invert__(self):  
                obj = type(self)()  
                obj.add(self, self.AND)  
                obj.negate()  
                return obj    
                
                  
            传Q对象,构造搜索条件
            首先还是需要导入模块:
            
            from django.db.models import Q
            传入条件进行查询:
            q1 = Q()
            q1.connector = 'OR'
            q1.children.append(('id', 1))
            q1.children.append(('id', 2))
            q1.children.append(('id', 3))
                
            models.Tb1.objects.filter(q1)
            合并条件进行查询:
            con = Q()
            
            q1 = Q()
            q1.connector = 'OR'
            q1.children.append(('id', 1))
            q1.children.append(('id', 2)) 
            
            q2 = Q()
            q2.connector = 'OR'
            q2.children.append(('status', '在线'))
            
            con.add(q1, 'AND')
            con.add(q2, 'AND')
            
            models.Tb1.objects.filter(con)
            
    -   Count
        用来做聚合查询
        比如想要得到某个分类下有多少篇文章？
        一对多反向查询
        表名小写_set
            #   category.post_set.count()
        
        categories = Category.objects.annotate(posts_count=Count("post"))
        print(categories[0].posts_count)    // 相当于给category动态地增加了posts_count属性
        
    -   Sum
        统计所有文章加起来的pv量
        Post.objects.aggregate(all_pv=Sum('pv'))
        # 输出结果类结果{‘all_pv’:372} 
        
        
        -   annotate        增加属性
        -   aggregate       直接计算结果
        
    -   Avg
    -   Min
    -   Max
        
        
    
    
#   数据库访问优化
    -   使用with模板标签
        在模板中使用QuerySet缓存，需要使用with标签

    -   使用iterator()
        获取大量数据时
        
        news_list = News.objects.filter(title__contains=u'违法')
        for news in news_list.iterator():
            print(news)
            
    -   使用 F() object query expressions 在同一模型中使用不同字段进行对比过滤

        # 查询所有title和sub_title相同的数据
        queryset = News.objects.filter(title=F('sub_title'))
        使用 QuerySet.extra()
    -   显式的执行SQL语句

        cl = Channel.objects.filter(parent__id=1).extra(
            select={
                'another_news_count': 'SELECT COUNT(*) FROM web_news WHERE web_news.channel_id = web_channel.id'
            }
        )
        
        print cl[0].another_news_count
        
    -   使用原生的SQL
        cl = Channel.objects.raw('SELECT * FROM web_channel WHERE parent_id = 1')
        print cl
        # <RawQuerySet: 'SELECT * FROM web_channel WHERE parent_id = 1'>
        for c in cl:
            print c
            
            
    -   预加载数据
        尽量一次加载你需要的数据
        
        QuerySet.select_related() , 针对foreign key 和 one-to-one
        news = News.objects.select_related().get(id=372924135)
        print news.channel # 不会访问数据库
        QuerySet.prefetch_related() , 1.4中存在, 和select_related()类似，针对many-to-many
        
        
    -   不要过度使用 count() 和 exists()
    
        比如，假设有一个Email的model，有一个 body 的属性和一个多对多关系的User 属性，下面的模板代码是最优的：
        
        {% if display_inbox %}
          {% with emails=user.emails.all %}
            {% if emails %}
              <p>You have {{ emails|length }} email(s)</p>
              {% for email in emails %}
                <p>{{ email.body }}</p>
              {% endfor %}
            {% else %}
              <p>No messages today.</p>
            {% endif %}
          {% endwith %}
        {% endif %}
        它是最优的是因为：
        
        因为QuerySet是惰性的，如果 'display_inbox' 是False的话，这不会产生数据库查询。
        
        使用 with 意味着我们会存储 user.emails.all 在一个变量中供后面使用，这允许被缓存以便重用。
        
        {% if emails %} 其实是调用 QuerySet.__nonzero__() ，在数据库层面执行 user.emails.all() ，然后返回结果，放入缓存。
        
        {{ emails|length }} 的使用将调用 QuerySet.__len__(),数据已在缓存
        
        for 循环的email数据已经在缓存中了。
        
        with的使用是关键
        每次的QuerySet.count()调用都会产生查询