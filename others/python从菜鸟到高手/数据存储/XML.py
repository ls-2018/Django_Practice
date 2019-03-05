# from xml.etree.ElementTree import parse
#
# doc = parse('./xml.xml')
# for item in doc.iterfind('products/product'):  # 通过XPath 搜索子节点集合,然后对这个子节点进行迭代
#     id = item.findtext('id')
#     # 读取节点的子节点的值要使用findtext
#     print(item.get('uuid'))# 读取当前及诶单下使用get方法
#     print(id)


# 字典------------> xml
import dicttoxml
from xml.dom.minidom import parseString
import os

d = [20, 'names',
     {'name': 'bill', 'age': 12, 'salary': 1230},
     {'name': 'bill', 'age': 12, 'salary': 1230},
     {'name': 'bill', 'age': 12, 'salary': 1230}]
# 将字典转换为xml(bytes)形式
bxml = dicttoxml.dicttoxml(d, custom_root='persons')
xml = bxml.decode('utf-8')  # 将bytes形式的数据----->utf8
print(xml)

dom = parseString(xml)
prettyxml = dom.toprettyxml(indent='    ')  # 生成带锁紧格式的XML字符串
f = open('person.xml', 'w', encoding='utf8')
f.write(prettyxml)
f.close()



# xml------------> 字典
import xmltodict
import pprint
f = open('person.xml','rt',encoding='utf8')
xml = f.read()
d= xmltodict.parse(xml)
f.close()


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)
