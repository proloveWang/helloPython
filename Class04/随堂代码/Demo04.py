#定义函数，实现功能：判断一个数字是不是质数
def isZhiNum(num):
	i = 2
	while i < num:
		if num % i == 0:
			return False
		i += 1
	return True

print(isZhiNum(8))

# 7. 编写一个函数，接受一个字符串作为参数，并返回一个新的字符串，其中每个字符都重复3次。
def getThree(str):
	newStr = ""
	for s in str:
		newStr += s*3
	return newStr
print(getThree("abc"))

# 8. 编写一个函数，接受一个字符串和一个字符作为参数，并返回该字符串中该字符的出现次数。
def getCount(str,char):
	count = 0;
	for s in str:
		if s == char:
			count += 1
	return count

print(getCount("aaabbbccc","a"))
# 直接调用str的方法
print("aaabbbccc".count("a"))