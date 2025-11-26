# 1. 判断字符串的内容是否为纯数字
s = '1230'
res = s.isdigit()
print(res)  # True

s = '1230 '
print(s.isdigit())  # False

# 2. 判断字符串的内容是否为纯字母
# 字母：世界各国语言 统称为字母
s = 'abc你Вㅘタ'
res = s.isalpha()
print(res)  # True

# 4. 判断字符串中的英文字母是否为大写字母
s = 'her12324'
res = s.isupper()
print(res)  # False

s1 = 'HER12324'
res = s1.isupper()
print(res)  # True

# 5. 判断字符串中的英文字母是否为小写字母
res = s.islower()
print(res)  # True
res = s1.islower()
print(res)  # False

# 6. 判断字符串的内容是否满足 单词的首字母大写 其他小写
s = 'Good Nice 13'
res = s.istitle()
print(res)  # True

s1 = 'Good nice 13'
res = s1.istitle()
print(res)  # False

# 7. 判断字符串的内容是否是ASCII码符号
print(s.isascii())  # True

# 8. 判断字符串的内容是否已指定内容开头
# res = 'good good study'.startswith(指定内容)
'''
指定内容的数据类型：
	1. 字符串  验证是否以指定的字符串开头
	2. (字符串1，字符串2, 字符串3)  元组类型的数据   判断字符串的内容是否以其中一个开头
'''
res = 'good good study'.startswith('good')
print(res)  # True

res = 'Good good study'.startswith('good')
print(res)  # False

res = 'Good good study'.startswith(('good', 'Good', 'GOOD'))
print(res)  # True

# 9. 判断字符串的内容是否已指定内容结尾
'''
1. 字符串  验证是否以指定的字符串结尾
2. (字符串1，字符串2, 字符串3)  元组类型的数据   判断字符串的内容是否以其中一个结尾
'''
res = 'good good study'.endswith('dy')
print(res)

res = 'good good stuDy'.endswith(('dy', 'Dy', 'DY', 'dY'))
print(res)