# 函数作为参数传递
# 传递的是计算的逻辑，而非数据
def add(a, b):
	return a + b


def cheng(a, b):
	return a * b


def showFuntion(functionName):
	res = functionName(2, 3)
	return res


# 传递了一个函数的对象，不是函数的调用,不要添加函数的括号，看见括号是函数的调用
result = showFuntion(add)
print(result)

result = showFuntion(cheng)
print(result)

# 假如我定义了一个函数，这个函数只被调用了一次，定义岂不是浪费时间吗？
# 使用匿名函数，传递到方法的体内
#                    lambda 传入参数:函数体(一行代码)
result = showFuntion(lambda x, y: x ** y)
print(result)
