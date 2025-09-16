# 位置参数 定义一个函数，在调用的时候，不管是个数还是数据类型，都要一致 （我们见过的最常见的方式）
def fun1(x):
	print(x)

fun1(100)

# 关键字参数   使用键值对，传递参数，即使位置传递的不一样，也不影响
def fun2(x, y, z):
	print(f"{x} {y} {z}")


# 如果使用位置参数传参
fun2(1, 2, 3)
# 使用关键字传参
fun2(z=300, y=200, x=100)


# 缺省参数  也叫做默认值传参，相当于参数指定了默认值，可以传递也可以不给默认值传递
def fun3(a, b=20):
	return a + b


def fun4(a=1, b=20):
	return a + b


"""
这个写法是错误的，假如两个参数只有一个有默认值，这个参数必须放在最后面
def fun5(a=1, b):
	return a + b
"""

# 缺省值传参 假如两个都有默认值，直接给第一个
print(fun4(10))
# 位置传参
print(fun3(10, 30))
# 关键字传参
print(fun3(b=30, a=300))


# 不定长参数
def fun5(x, *y):
	print(x, y)


def fun6(*y):
	print(y)


# 以下这个写法是错误的，可变长参数，必须放在普通参数的后面，否则运行报错
""""""
def fun7(*y, x):
	print(x, y)


fun5(1, 2, 3, 4, 5)
fun6(1, 2, 3, 4, 5)

fun7(1, 2, 3, 4, 5,x=6)

# 可变长度的关键字传递，使用到了kwargs 关键字
"""
  可变长度的关键字传递 使用 两个** 修饰一个变量名，一般叫做kwargs，也可以不叫这个名字
  kwargs 接收多个kv键值对，并且可以通过 in 判断 参数中是否还有某个key值。 
"""


def showMsg(name, age, **kwargs):
	if "job" in kwargs:
		print("kv键值对中含有job字样")
		print(name, age, kwargs)
		return
	if "city" in kwargs:
		print("kv键值对中含有city字样")
		print(name, age, kwargs)
		return


showMsg("zhangsan", 19, job="大数据工程师")
showMsg("zhangsan", 19, city="国际郑")
showMsg("zhangsan", 19, address="大郑州")
showMsg("zhangsan", 19, address="大郑州", hobby="打篮球")


# 这个调用时错误的  **kwargs 必须接收 kv键值对的参数，否则报错
# showMsg("zhangsan", 19, "大郑州", "打篮球")

def showMsg2(name, age, *, job, city):
	print(name, age, job, city)


def showMsg3(name, age, *, job="鉴黄师", city):
	print(name, age, job, city)


showMsg2("zahgnsan", 18, job="BI工程师", city="魔都")
# 由于限制了 key 必须是 job city 所有，以下报错
# showMsg2("zahgnsan", 18, address="BI工程师", city="魔都")
# 由于 * 后面限制了，kv键值对必须是两个值，所有传递一个，报错！
# showMsg2("zahgnsan", 18, job="BI工程师")
showMsg3("张自力", 19, job="入殓师", city="上海")


# 如果存在关键字参数必须在可变参数的后面
def showMsg3(x, *y, **z):
	print(x)
	print(y)
	print(z)


showMsg3(1, 2, 3, job="寻找外星文明", city="三里屯")

# 命名关键字参数不能和可变参数共存
"""
def show9(x,*y,*,z,a):
	print("xxxxx")
"""
