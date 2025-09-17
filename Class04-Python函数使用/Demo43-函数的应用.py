
# 所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数
def testB():
	print('---- testB start----')
	print('这里是testB函数执行的代码...(省略)...')
	print('---- testB end----')

def testA():
	print('---- testA start----')
	testB()
	print('---- testA end----')
testA()
#-------------------
print("-------------------")
#-------------------

# 函数的递归
# 使用递归算法，求出任意数的和
def toSum(num):
    if num == 1:
        return 1
    else:
        return num+toSum(num-1)
sum = toSum(10)
print(sum)
"""
有六个人,第六个人说他比第五个人大3岁,第五个人说他比第四个人大3岁,第四个人说他比第三个人大3岁,
第三个人说他比第二个人大3岁,第二个人说他比第一个人大3岁,第一个人说自己13岁,求第六个人多大
"""
def sumAge(n):
    if n == 1:
        return 13
    else:
        return sumAge(n-1)+3
sum2 = sumAge(6)
print(sum2)

#-------------------
print("-------------------")
#-------------------

#递归进阶操作：斐波那契数列
# 斐波那契数列（Fibonacci）最早由印度数学家戈帕拉（Gopala）提出，而第一个真正研究斐波那契数列的是意大利数学家 Leonardo Fibonacci，斐波那契数列的定义很简单，数列的前两位数字是1，之后的数由前两个数相加而得出，例如斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def getFibonacci(index):
    if index == 1 or index == 2:
        return 1
    return getFibonacci(index - 1) + getFibonacci(index - 2)

for i in range(1, 15):
    print(getFibonacci(i), end=", ")

#-------------------
print("-------------------")
#-------------------

# 高级: 函数多返回值
def test():
    # 在返回多个数据时 可以使用【return 数据1,数据2,...】的方式进行多个数据返回，同时还支持不同类型数据
    return 1,"2"
# 在接收函数返回多个数据时，提供的存储数据变量需要按照返回值顺序，写对应顺序的多个变量接收即可，变量与变量之间使用【逗号】分隔
x,y = test()
print(x)
print(y)

# 一个函数中可以有多个return语句，但是只要有一个return语句被执行到，那么这个函数就会结束了，因此后面的return没有什么用处
# return后面可以是元组，列表、字典等，只要是能够存储多个数据的类型，就可以一次性返回多个数据
# 如果return后面有多个数据，那么默认是元组【其实可以使用一个变量接收return返回多个数据值，但是一个变量接收的结果默认是元组】
y = test()
print(y)
# -------------输出结果-------------
# (1, '2')




