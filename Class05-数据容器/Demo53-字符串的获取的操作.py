s = r'Welcome to yhedu study'

'''
1. 在指定范围中 查询子串第一次出现的位置
	字符串对象.index(子串, 起始位置, 结束位置)  --- 找不到报错
	字符串对象.find(子串, 起始位置, 结束位置)  --- 找不到 返回的是-1

	子串是多个符号 获取的是第一个符号的下标
'''
# 不规定查找范围  从左到右整体查询
pos = s.index('s')
print(pos)
# 对'也有转义的意思  在字符串要展示的内容中 要呈现 '
# 王籽澎的昵称是 '隔壁老王'
message = '王籽澎的昵称是 \'隔壁老王\''
print(message)

# 从指定位置开始进行查找
pos = s.index('s', 3)
print(pos)

# 指定开始与结束[不包含]
# pos = s.index('s', 3, 8)
# print(pos)  # ValueError: substring not found

s1 = 'noodle too'
pos = s1.index('oo')
print(pos)  # 1

pos = s.find('s', 3, 8)
print(pos)  # -1

'''
2. 在指定范围中 查询子串最后一次出现的位置
	字符串对象.rindex(子串, 起始位置, 结束位置)  --- 找不到报错
	字符串对象.rfind(子串, 起始位置, 结束位置)  --- 找不到 返回的是-1

	子串是多个符号 获取的是第一个符号的下标
'''
pos = s.rfind('s')
print(pos)  # 17

pos = s.rfind('s', 0, 10)
print(pos)  # -1

'''
3. 在指定范围中 查询子串出现的次数
	字符串对象.count(子串, 起始位置, 结束位置)
'''
pos = s.count('s')
print(pos)  # 1

# 指定起始 到末尾开始查找
pos = s.count('s', 8)
print(pos)  # 1

pos = s.count('s', 8, len(s))
print(pos)  # 1

pos = s.count('s', 18, len(s))
print(pos)  # 0