# 替换
'''
字符串数据.replace(旧子串, 新子串, 个数)
	旧子串 --- 要替换掉的
	新子串 --- 要替换成的
	个数 --- 不设置的换 默认全部替换
'''
s = 'good good god'
new_s = s.replace('g', 'G')
print(new_s)  # Good Good God

new_s = s.replace('g', 'G', 1)
print(new_s)  # Good good god

new_s = s.replace(' ', '_')
print(new_s)  # good_good_god

print("#----------------------------移除")
'''
移除的是两端的内容
	字符串数据.strip(指定内容)  移除字符串两端的指定内容
	字符串数据.lstrip(指定内容) 只移除左端的指定内容
	字符串数据.rstrip(指定内容) 只移除右端的指定内容

指定内容没有设置 移除的是任意的空白符号
'''
s = ' \t\r\nabc\t\t\tgood \n'
new_s= s.strip()
print(new_s)  # abc	good

s = '@#$%^abc\t\t\tgood^%$#'
new_s = s.strip('@#$%^&*')  # 左右逐个获取 验证是否在指定的内容中 在的话移除 不在话停止移除操作
print(new_s)  # abc	good

s = '@#$%^abc\t\t\tgood^%$#'
new_s = s.lstrip('@#$%^&*')  # 左右逐个获取 验证是否在指定的内容中 在的话移除 不在话停止移除操作
print(new_s)  # abc	good^%$#

s = '@#$%^abc\t\t\tgood^%$#'
new_s = s.rstrip('@#$%^&*')  # 左右逐个获取 验证是否在指定的内容中 在的话移除 不在话停止移除操作
print(new_s)  # @#$%^abc	good