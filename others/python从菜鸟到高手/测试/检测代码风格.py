'''
# PyLint
# 检测代码风格
pip3 install pylint
pylint 检测代码风格.py
'''
from flake8.api import legacy as flake8

# 忽略错误表示F401和W503
style_guide = flake8.get_style_guide(ignore=['F401', 'W503'])
# 对此脚本进行检测
style_guide.check_files(['检测代码风格.py'])


def xxx():
    '''
    xxxx
    :return:
    '''

    print(123)


# if __name__ == '__main__':
#     xxx()


# ##############Flake8#####################
'''
http://flake8.pycqa/en/latest/user/index.html
pip3 install flake8
用法和pylint一样,不用指定-v
flake8 --select F401 test.py    只检测指定错误,  多个以,分割
'''
