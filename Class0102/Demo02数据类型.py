# 先将一个数据存在一个变量中，为了以后使用
# num1 = 100 这个是存储在内存中
num1 = 100
num2 = 80
# 变量不使用，没有意义
num3 = num1 + num2
print(num3)

# 字符串
num4 = 'abc'
# 布尔 true false
isNull = True
# 浮点型
sal = 18.7

# 如何知道一个变量的类型呢？ 使用 type(变量的名称) 就能知道这个变量的类型
print(type(sal))
print(type(num3))

# 在python中 变量类型不显示的的写出来，而是通过值推断变量的类型的
# python 中  a = 10
# 在其他语言中，比如java  int a = 10;

# 标⽰符由字⺟、下划线和数字组成，且数字不能开头





# 错误演示：
# True = 10
# 0abc = 20
# from#12 = 10
# my-Boolean
# test!32
# haha(da)tt
# jack&rose
# G.U.I
gui = 10
gui = 20
# 通过这个案例想说明： python的变量是区分大小写的
GUI = 30
print(gui)

