#   virtualenv的增强包
    
    -   pip install virtualenvwrapper  
    -   修改用户家目录下的.basgrc文件。如果是oh-my-zsh用户，则需修改.zshrc最后一行添加以下内容
    -   export  WORKON_HOME=$HOME/.virtualenvs
    -   source /usr/local/bin/virtualenvwrapper.sh
    
    如果使用 --user安装
    -   source $HOME/.local/bin/virtualenvwrapper.sh
 
    -   mkvirtualenv   project-env
    -   cd project-env
    -   source bin/active
    -   deactive