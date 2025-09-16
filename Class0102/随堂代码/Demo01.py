print("hello 大数据")
# 单行注释
'''
多行注释，可以写多行，可以拐弯的注释
'''
# python是一个解释性的弱语言，它不是没有数据类型，而是根据值推断变量的类型的
# 这个现象跟js 非常像
name = "张三"
age = 20
print(type(name))
# ctrl + d 是复制一行的意思
print(type(age))
num = 1
num2 = 3
# 变量的使用
print(num + num2)

# string 类型是单引号还是双引号？答案是都可以，python 中没有char 类型
name = 'lisi'
print(name)
isNull = True  # boolean 类型首字母是大写的

# import 导入一个模块（导入包的意思）
import keyword

# 返回所有的python的关键字
print(keyword.kwlist)

# python变量是区分大小写的
NAME = '王五'
print(NAME)
print(name)
