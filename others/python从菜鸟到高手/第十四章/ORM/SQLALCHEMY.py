'''
sqlalchemy 和 sqlobject

sqlalchemy 更接近于sql 语句;对对象的抽象化非常完美,可以更灵活地提交原生的SQL语句
sqlobject  更接近Python,更快速


pip3 install SQLAlchemy
pip3 install mysql-connector
'''
from sqlalchemy import (
    create_engine,
    MetaData,
    Table, Column, Integer, String, Float,
    exc, orm

)
from sqlalchemy.ext.declarative import declarative_base

########################连接数据库##################################
# 定义连接字符串
mysql = 'mysql+pymysql://root:1234@localhost:3306/demo?charset=utf8'
# 创建数据库引擎(sqlalchemy.engine.base.Engine对象)
engine = create_engine(mysql, encoding='utf-8')
engine.connect()
########################创建表#####################################
'''
由于创建表需要指定表的元数据,也就是字段名\\字段数据类型等信息,所以要先创建Metadata对象,该对象通过构造方法的参数与engine关联,
然后再通过一个Table对象用于指定表中字段的相关信息,Table对象需要与Metadata对象关联,最后调用metadata对象的create_all方法来创建表.
'''
# 创建MetaData对象
metadata = MetaData(engine)
person = Table('users', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String(20)),
               Column('age', Integer)
               )
# 创建表
metadata.create_all(engine)
########################创建会话(Session)##########################
# 任何数据库操作之前都需要创建session对象
Session = orm.sessionmaker(bind=engine)
session = Session()

######################定义与表对应的Python类#########################
# CURD分别对应一个类(继承declarative_base函数返回的Base类)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # 指定表名
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
##########################################################


########################连接数据库##################################


########################连接数据库##################################
