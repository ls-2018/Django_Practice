#   MarkDown第三方插件
    pip install mistune
    
    
    content = mistune.markdown(content)
        
    <div class="comment-content">
        {% autoescape off %}
        {{ comment.content }}
        {% endautoescape %}
    </div>
    
#   默认情况下 MarkDown 对我们的写代码放到<code>标签中，没做特殊处理，因此需要借助另外的工具
    1、谷歌的code-prettify
    2、highlight.js
    
    -   这里选择highlight.js，两者使用大同小异
    
    1、 
        <link rel="stylesheet" href="https://cdn.bootcss.com/highlight.js/9.12.0/styles/googlecode.min.css">
        <script src="https://cdn.bootcss.com/highlight.js/9.12.0/highlight.min.js"></script>    可以定制下载
        <script>hljs.initHighlightingOnLoad();</script>
        
        # 原理：通过Markdown贴的代码，会被渲染到<pre><code>    </code></pre>标签中，而highlight.js或者其他前端代码高亮的库
        会提取<code>块中的代码，然后进行分析，进而通过不同的标签进行包装，最后通过CSS展示不同的颜色
        
    
    
    Google代码高亮前端库的用法：https://github.com/google/code-prettify/blob/master/docs/getting_started.md
    highlight.js的用法  https://highlightjs.org