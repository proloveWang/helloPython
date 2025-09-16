def fun1():
	return 1
	return 2  # 碰到第一个return,直接函数就结束了，不会往下执行了


print(fun1())


def fun2():
	return 1, 2


a, b = fun2()
print(a, b)
# 假如一个函数返回值是多个，这个返回值的类型是 元组
# 元组  首先是一个集合，集合中的元素的类型可以不一样  ("a",18,98.87)
print(type(fun2()))
# c 此时不是一个值，是一个集合，元组
c = fun2()
print(c)
