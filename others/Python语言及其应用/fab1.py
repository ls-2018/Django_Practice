# def iso():
#     from datetime import date
#     print(date.today().isoformat())

from fabric.api import local
from   fabric.api import env
env.password = ''

def iso():
    local('ls')