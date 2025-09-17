name = "laoYan"
for x in name:
	if x == 'a':
		continue
	print(x)
else:
	print("已经到最后了，没数据了")
# else 只有在循环执行完毕之后才能打印，假如是半道结束的，是不会打印else语句的


# for - in 的用法
# [0,5)
for x in range(5):
	print(x)

# 从5开始到9 , [5,10)
for x in range(5,10):
	print(x)
# 步长可以从1变为别的，比如2
for x in range(5,10,2):
	print(x)
# 数组还可以倒着创建 [10,5)
for x in range(10,5,-1):
	print(x)
# 这个集合中都是空数据
for x in range(10,5,1):
	print(x)