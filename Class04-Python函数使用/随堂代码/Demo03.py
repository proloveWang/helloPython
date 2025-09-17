"""
有六个人,第六个人说他比第五个人大3岁,第五个人说他比第四个人大3岁,第四个人说他比第三个人大3岁,
第三个人说他比第二个人大3岁,第二个人说他比第一个人大3岁,第一个人说自己13岁,求第六个人多大
"""


# 递归的使用
def getAge(num):
	if num == 1:
		return 13
	return getAge(num - 1) + 3


print(getAge(6))


# 斐波那契数列
# 求前30个菲波那切数列的值
def feiBo(num):
	if num == 1 or num == 2:
		return 1
	else:
		return feiBo(num - 2) + feiBo(num - 1)


loop = 3
while loop <= 30:
	print(feiBo(loop), end=" ")
	loop += 1

a = 1
if type(a) == int:
	print("a 是一个整数")
else:
	print("a 不是一个整数")

if isinstance(a,int):
	print("a是一个整数类型")
else:
	print("a 不是一个整数")
