age = 19
if age >= 18:
	print("可以进入网吧")
	print("abc")
else:
	print("未成年人不能进网吧")
sex = "male"
if age >= 18 and sex == "male":
	print("免费进入")
else:
	print("给钱进入")

"""
班级的分数：
如果大于90分 是 A
大于80分     是 B
大于70分     是 C
大于60分     是 D
其他分数是   不及格
"""
# 不使用elif
score = int(input("请输入您的分数："))
if score >= 90:
	print("A")
else:
	if score >= 80:
		print("B")
	else:
		if score >= 70:
			print("C")
		else:
			if score >= 60:
				print("D")
			else:
				print("不及格")
# 使用elif
if score >= 90:
	print("A")
elif score >= 80:
	print("B")
elif score >= 70:
	print("C")
elif score >= 60:
	print("D")
else:
	print("不及格")

# 1 => spring, 2 => summer, 3 => autumn, 4 => winter
# 在编写的时候，不要添加空格键，直接输入tab，否则报错
# 类似java中的  switch
season = int(input("你最喜欢哪个季节："))
match season:
	case 1:
		print("春天，困！")
	case 2:
		print("夏天，热")
	case 3:
		print("秋天，乏")
	case 4:
		print("冬天，冷")
	case _:
		print("热爱学习")

"""
情节描述：上公交⻋，并且可以有座位坐下
要求：输⼊公交卡当前的余额，只要超过2元，就可以上公交⻋；如果空座位的数量⼤于0，就可以坐下
"""
yueE = 1
seatNum = 3
if yueE >= 2:
	if seatNum > 0:
		print("有座位，请入座")
	else:
		print("没座位，站着")
else:
	print("余额不足，欢迎下次光临！")
