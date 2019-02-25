#   WSGI        -       Web框架的基础
    
    -   WSGI全称是Web Server Gateway Interface(web服务器网关接口） 。 这是Python中定义的一个网关协议，规定了Web Server如何
        跟应用程序交互。Web Server可以理解为一个Web应用的容器，通过它可以启动应用，进而提供HTTP服务。而应用程序是指我们基于框架所开发的系统
    -   这个协议的最主要的目的就是保证在Python中所有的Web Server程序或者说Gateway程序，能够通过统一的协议跟Web框架或者说Web应用进行交互。
    
    
    -   使用统一协议的好处：Web应用框架只需要实现WSGI，就可以跟外部请求进行交互了，不用去针对某个Web Server来独立开发交互逻辑，开发者可以把经理放在框架本身。
    
    客户端  -------->     Web Server   ------------>   Web 应用
    
    客户端  -------------------------------wsgiref->   Web 应用           // wsgiref是WSGI协议的一种实现，但效率不高。
    
        
                                            
                                            