-   null            同blank对比考虑，其中null用于设定在数据库层面是否允许为空
-   blank           针对业务层面，该值是否为空
-   choices         配置choices，admin页面就可以看到对应的可选项展示
-   db_column       默认情况下，定义的Field就是对应数据库中的字段名名称，通过这个参数可以指定Model中某个字段对应数据库中哪个字段
-   db_index        索引配置
-   default         默认值配置
-   editable        是否可编辑，默认是True,如果不想将这个字段保存到页面上，可以配置为False
-   error_message   用来自定义字段值校验失败时的异常提示，他是字典格式。
    -   key的可选项为:
    -   null
    -   blank
    -   invalid
    -   invalid_choice
    -   unique
    -   unique_for_data

-   help_test       字段提示语，配置这一项后，在页面对应字段下方会展示此配置
-   primary_key     主键，一个model只允许一个字段设置此参数
-   unique          唯一约束。   unique=True后，不需要再在设置db_index=True
-   unique_for_date 针对date字段的联合约束，    unique_for_date="created_time"  并不是数据库层面的约束
-   unique_for_month
-   unique_for_year
-   unique_for_name 字段对应的展示文案
-   validators      自定义校验逻辑



#   https://docs.djangoproject.com/en/1.11/ref/models/fields/


erbose_name=None,
name=None,
primary_key=False,
max_length=None,
unique=False,
blank=False,
null=False,
db_index=False,
rel=None,
default=NOT_PROVIDED,
editable=True,
serialize=True,
unique_for_date=None,
unique_for_month=None,
unique_for_year=None,
choices=None,
required
help_text='',
db_column=None,
db_tablespace=None,
auto_created=False,
validators=(),
error_messages=None







在实际使用中，GenericForeignKey ； 唯一的问题是我们需要操作两个模型表，这多少会对性能有些影响，因此我们往往会想办法自己来实现对应的逻辑。
这其实也是基于通用性和特殊性之间的考虑，通用性能够得到更易用的逻辑，但是性能上会有损耗，而特殊性的处理逻辑在性能上会有一些优势，却降低了易用性
