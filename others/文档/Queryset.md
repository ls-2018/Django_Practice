#   QuerySet接口

#   支持链式调用的接口
    -   all
    -   filter
        -   filter(content_contains="条件")
        -   filter(content_icontains="条件")
    -   exclude     同filter相反的逻辑
    -   reverse     把queryset中的结果倒序排列
    -   distinct    去重
    -   none        返回空的queryset
    
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
    -   values          返回的结果包含dict的queryset
    -   values_list     返回的结果按查询字段的顺序的元组的queryset
    
    
    
    
#   高级接口
    -   defer           把不需要的字段做延迟加载
        posts = Post.objects.all().defer("content")
        for post in posts:      # 此时会执行数据库查询
            print(post.content)  # 此时会执行数据库查询，获取到content
        
        当不想加载某个过大的字段时（如text类型的字段，会使用defer），但上面的演示会产生N+1的查询问题，在实际使用时千万要注意。
                在外键查询时也会产生N+1的问题
            
      
    -   only            与defer相反，只获取only里的字段，再获取其他值得时候，会产生额外的查询
    
    
    -   select_related  
        用来解决外键产生的N+1的问题的方案。

        posts = Post.objects.all().defer("content")
            for post in posts:      # 产生数据库查询
                print(post.owner)   # 产生额外的数据库查询,关联表 owner
        
        posts = Post.objects.all().select_related('category')
            for post in posts:      # 产生数据库查询，category也会一次性查询出来
                print(post.category)    #   相当于连表操作
        
        当然这个接口，只能用来解决一对多的关联关系。
    
    -   prefetch_related    
        
        
        
        
                    




