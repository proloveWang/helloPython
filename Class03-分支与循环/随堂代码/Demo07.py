# 打印5次hello world
num = 5
while num >= 1:
	print("hello world")
	num -= 1

# 计算1~100的累积和（包含1和100） 5050
sum = 0
loop = 1
while loop <= 100:
	sum = sum + loop
	loop += 1
print(sum)

# 计算1~100之间偶数的累积和（包含1和100）
loop = 1
sum = 0
while loop <= 100:
	if loop % 2 == 0:
		sum = sum + loop
	loop += 1
print(sum)

"""
 *
 * *
 * * *
 * * * *
 * * * * *
"""
m = 1
# 最外层控制行数
while m <= 5:
	n = 1
	while n <= m:
		print("*", end=" ")
		n += 1
	m += 1
	print()

# 补充的内容
print("-" * 100)

# 打印99乘法表
# -2d的意思是：宽度是两位，不够两位补空格，-的意思是数字后面补空格，不加-，数字前面补空格
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print("%d*%d=%-2d" % (j, i, (i * j)),end=" ")
		j += 1
	print()  # 换行的意思
	i += 1


print("%02d"%(1))
print("%.2d"%(1))