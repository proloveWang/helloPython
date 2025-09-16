'''
int(x [,base ])    将x转换为一个整数
long(x [,base ])    将x转换为一个长整数
float(x)    将x转换到一个浮点数
complex(real[,imag])    创建一个复数
str(x)    将对象 x转换为字符串
repr(x )    将对象x转换为表达式字符串
8 eval(str)    用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )    将序列s转换为一个元组
10 list(s )    将序列s转换为一个列表
11 chr(x)    将一个整数转换为一个字符
12 unichr(x)    将一个整数转换为Unicode字符
13 ord(x)    将一个字符转换为它的整数值
14 hex(x)    将一个整数转换为一个十六进制字符串
15 oct(x)    将一个整数转换为一个八进制字符串
'''
###########################################
print("请输入第一个数字：")
num1 = input()
#num1 = int(num1)
print("请输入第二个数字")
num2 = input()
#num2 = int(num2)
print("计算的结果为%d" % (num1 + num2))
# 运行报错：
# Traceback (most recent call last):
#   File "D:\yangeworkspace\pythonProject\_07两个数值相加.py", line 7, in <module>
#     print("计算的结果为%d" % (num1 + num2))
# TypeError: %d format: a real number is required, not str
# 原因是num1 和 num2 都是Str类型，无法运算
# 要进行数据类型转换：
print("请输入第一个数字：")
num1 = input()
num1 = int(num1)
print("请输入第二个数字")
num2 = input()
num2 = int(num2)
print("计算的结果为%d" % (num1 + num2))
###########################################
name = "zhangsan"
age = 10
print("name=%s,age=%d"%(name,age))
# 字符串是可以拼接的
name2 = "lisi"
# 字符串拼接，字符串拼接使用 + 号
print("两个人的名字是："+name+","+name2)
# 格式化输出
print("两个人的名字是：%s,%s"%(name,name2))
#  字符串中的+ ,必须左右两边都是字符串，不能是其他字符
# print("name="+name+",age="+age)   错误演示
print("name="+name+",age="+str(age))
#print(name+age)
###########################################
#  float => int   str => int
a = int(3.14)
b = int("1")
# c = int('y')
print(type(a))
print(type(b))

a = float(3)
b = float("3.14")
print(type(a))
print(type(b))

a = str(100) # 100 => '100'
b = str(3.14) # 3.14 => 3.14

# bool 里面只要不是空的，或者不是0 就都返回True
a = bool(1)
b = bool(0)
print(a)
print(b)
a = bool(100)
print(a)
b = bool("hello")
print(b)