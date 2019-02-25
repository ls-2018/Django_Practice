-         在开发企业开发内部系统时，往往需要集成已有的SSO(Single Sign-On ，单点登录）系统进来。集成登录的逻辑只需要参考
        Django默认的settings的配置AUTHENTICATION_BACKENDS是如何实现的即可，
        
        
        
-   如果已经集成了SSO，权限部分的逻辑怎么处理
    -   在自定义的    AUTHENTICATION_BACKENDS    中来做
    -   在django admin来做
    
        -   has_add_permission
        -   has_change_permission
        -   has_delete_permission
        -   has_module_permission
            都是返回True\False
    
           
        