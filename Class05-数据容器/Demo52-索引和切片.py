# 索引就是表名字符串中存储字符对应的位置
# Python对于序列的索引有两种方式的操作：
# 1. 正向索引 【从左向右数】范围是[0, 长度N-1]
# 2. 负向索引 【从右向左数】范围是[-1, -N-1] --- 递减数列
# 对于有序序列来说，想要定位获取或者修改序列中的元素，就需要索引来进行定位，格式: 序列[索引]

# len(序列) --》可以获取序列的长度
s = '\n'
print(len(s))  # 1
s1 = r'\n'
print(len(s1))  # 2

s = r'Welcome to yhedu study'
print(len(s))  # 22

# 获取第一个字符
print("----------获取第一个字符")
ch = s[0]  # 定位到之后赋值给变量
print(ch)  # W
print(s[-1])  # y
print(s[-22])  # W

# 负向索引
print("----------负向索引")
ch = s[-len(s)]
print(ch)  # W

# 获取最后一个字符
print("----------获取最后一个字符")
last_ch = s[len(s) - 1]
print(last_ch)  # y

last_ch = s[-1]
print(last_ch)  # y


# 获取倒数第三个字符
last_ch_3 = s[-3]
print(last_ch_3)
print(s[len(s) - 3])

s = r'Welcome to yhedu study abc'
print(len(s))  # 22
# s[0] = 'w' # ERROR

# # 字符串是不允许发生变化【不可变】
# # s[0] = 'w'  # 修改这个位置的元素
# # TypeError: 'str' object does not support item assignment
# # 类型错误：字符串对象不支持元素被指派内容


print("------------------------------------------切片")
# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 通过索引定位范围区域，在这个区域中提取相关的子串信息，切片的操作是序列[起始索引:结束索引:步长]
# 起始索引和结束索引只是定位范围的，使用正向索引和负向索引均可
# 根据步长的正负情况切片是分为两种的
# 1. 正向切片 【从左向右提取子串】步长是为正数，起始索引定位的字符应该在结束索引定位的左边从起始索引定位的字符开始 按照步长 获取相应的字符，注意不包含结束索引对应的位置
# 2. 负向切片 【从右向左提取子串】步长是负数，起始索引定位的字符应该在结束索引定位的右边从起始索引定位的字符开始 按照步长 获取相应的字符，注意不包含结束索引对应的位置
# 切片的操作中有些内容是可以省略的：
# 1. :步长可以省略，表示步长为1
# 2. 起始索引可以省略，如果是正向切片 表示从最左边开始， 如果是负向切片 表示从最右边开始
# 3. 结束索引可以省略，如果是正向切片 表示到最右边结束，如果是负向切片 表示到最左边结束

s = 'Welcome to yhedu study'
print(s[0:len(s):1]) #Welcome to yhedu study
print(s[:]) #Welcome to yhedu study
print(s[::1]) #Welcome to yhedu study
print(s[::])  #Welcome to yhedu study

# 将字符串倒过来
print(s[::-1])  # yduts udehy ot emocleW
print(s[len(s)-1::-1]) # yduts udehy ot emocleW
print(s[-1:-len(s)-1:-1]) # yduts udehy ot emocleW

sub_s = s[:3]  # 提取前3个
print(sub_s)  # Wel


sub_s = s[-3:]  # 提取的是后3个字符
print(sub_s)  # udy

sub_s = s[-3::-1]
print(sub_s)  # uts udefq ot emocleW

sub_s = s[1:-1:-1]
print(sub_s)  # ''

# s = 'Welcome to yhedu study'
#      W l o e t * h d * t d   # *代表空格
sub_s = s[::2]
print(sub_s)  # Wloet hd td









