def fun1(x):
	def fun2(y):
		return x + y

	return fun2


print(fun1(2)(3))

# 既要计算每个数据的二次方，又要计算每个数据的三次方
data = [1, 2, 3, 4, 5, 6]
from math import pow


def get_result(n):
	def do_pow(x):
		return pow(x, n)

	return do_pow


print(get_result(3)(2))
for i in data:
	print(get_result(3)(i))
