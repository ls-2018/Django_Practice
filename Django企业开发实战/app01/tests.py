#  使用sqlite,django 会创建一个机遇内存的测试数据库，用于测试。这意味着测试中所创建的数据，对开发环境或线上环境是没有影响的
#  Mysql，django会直接用配置信息，创建一个名为 test_student_db的数据库，用于测试。        因此需要保证有建表和建库的权限
#
# "TEST": {
#    'NAME': 'mytestsdatabase'
# }


from django.test import TestCase, Client
from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        """用来初始化环境，包括创建初始化的数据，或者做一些其他的准备工作"""
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@qq.com',
            profession='程序员',
            qq='111',
            phone='12138'
        )

    def test_creat_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex='1',
            email='nobody@dd.com',
            profession='程序员',
            qq='21',
            phone='3213'
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='huy1ang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='21',
            phone='3213'
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        print(students[0].get_sex_display())
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        # 测试首页可用性
        client = Client()
        response = client.get("/admin")
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='cxy',
            qq='222',
            phone='3222'
        )
        response = client.post("/", data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')
        response = client.get("/")
        self.assertTrue(b'test_for_post' in response.content, "response content must contain `test_for_test`")

    def tearDown(self):
        """用来清理测试环境和测试数据，在Django中，我们可以不关心这个"""
        pass
