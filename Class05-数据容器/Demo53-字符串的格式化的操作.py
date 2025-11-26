# 1. 按照指定宽度 对展示的字符串内容填充数据 【居左右填充  居右左填充  居中左右填充】
s = 'hello'
print(s)
# 居左右填充
# new_s = s.ljust(宽度, 填充符)  # 填充符默认是空格
new_s = s.ljust(10)
print(new_s)   # 'hello     '

new_s = s.ljust(10, '-')
print(new_s)  # hello-----

# 居右左填充
new_s = s.rjust(10)
print(new_s)  # '     hello'
new_s = s.rjust(10, '*')
print(new_s)  # '*****hello'

# 居中
new_s = s.center(10)
print(new_s)  # '  hello   '
new_s = s.center(10, '+')
print(new_s)  # '++hello+++'

# 2. 按照指定宽度 对字符串进行右对齐 左边填充0
s = '10'
new_s = s.zfill(10)
print(new_s)  # 0000000010

# 3. 引号嵌套的问题***  【展示的内容中有双引号  字符串数据就采用单引号包含 】
# 展示的内容中有单引号  字符串数据就采用双引号包含
s = "王籽澎的昵称是 '隔壁老王'"
print(s)

s = '王籽澎的昵称是 "隔壁老王"'
print(s)

# 有冲突的情况 内外引号情况一样 解决方式就是对内部引号采用转义符转义  取消掉字符串标记的含义
s = '王籽澎的昵称是 \'隔壁老王\''
print(s)

# 4. 字符串内容比较长 *** 可以直接换行写多个字符串 会自动拼接在一起  使用\把多个字符串连接在一起  形成一个
s = '其中五六只虾已熟透发红。方女士称，当天气温41度，' \
	'可能是自己把虾往地上和电动车后座放了的缘故，温度太高虾被烫熟了，' \
	'觉得十分搞笑。感慨这天气能不出门就不出门，待在空调房里最香。'
print(s)

s = '其中五六只虾已熟透发红。方女士称，当天气温41度，可能是自己把虾往地上和电动车后座放了的缘故，温度太高虾被烫熟了，觉得十分搞笑。感慨这天气能不出门就不出门，待在空调房里最香。'
print(s)

# 5. 字符串格式化
'''
除了%运算符之外  字符串也提供了相应的操作

字符串对象.format(填充的数据)
这种格式化方式，字符串对象里面的未知数据的占位符采用的是{}
'''
print("#################字符串对象")
name = '王籽澎'
gender = '男'
age = 21
score = 79.9
message = '这个人叫%s, 今年%d岁 性别是%s  成绩是%f' % (name, age, gender, score)
print(message)

message = '这个人叫{}, 今年{}岁 性别是{}  成绩是{:.2f}'.format(name, age, gender, score)
print(message)
print('这人{}, 今年{} 性别{} 成绩{:.0f}'.format(name, age, gender, score))

''' *******
Python3.6出现了简化操作  使用f或者F修饰字符串  在需要填充数据的地方 直接 {数据}
'''
message = f'这个人叫{name}, 今年{age}岁 性别是{gender} 成绩是{score:.2f}  学号{10:0>6} 千位分割{12345678987654567:,}'


print(message)

value = input('请输入数据：')
# 打印出来的信息是 value=数据值
info = f'{value=}'  # 3.8中新增的
print(info)  # value='19'