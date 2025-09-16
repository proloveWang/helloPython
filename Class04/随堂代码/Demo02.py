# 函数根据有无返回值和有无参数，可以分为四种情况
# 无参数无返回值
def fun1():
	print("欢迎来到王者荣耀")
	print("敌军还有5秒到达战场！")
	print("*" * 100)


fun1()


# 无参数有返回值
def fun2():
	print("进行温度测算进行中.....")
	return 24.5


temperure = fun2()
print(temperure)


# 有参数无返回值
def fun3(num):
	"""
	:param num: 打印乘法口诀的数量
	:return: 什么 都没有 None
	"""
	i = 1
	while i <= num:
		j = 1
		while j <= i:
			print("%d*%d=%-2d" % (j, i, (i * j)), end=" ")
			j += 1
		print()  # 换行的意思
		i += 1


fun3(5)


# 有参数有返回值
def fun4(a, b):
	"""
	:param a: 第一个值
	:param b: 第二个值
	:return: 两个数之和
	"""
	return a + b


print(fun4(3, 5))


def fun5():
	a = fun4(10, 20)
	return a


print(fun5())
