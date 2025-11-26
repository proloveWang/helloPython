# 切割： 以指定子串为切割点 将字符串分成n段
'''
字符串数据.split(切割符, 切割次数)  没有设置切割次数 能切几次切几次
	从左开始查找切割点 进行切割的

字符串数据.rsplit(切割符, 切割次数)  没有设置切割次数 能切几次切几次
	从右开始查找切割点 进行切割的
'''
s = 'hello nice   to meet you'
# 以 'e'为切割点
sub_list = s.split('e')
print(sub_list)  # ['h', 'llo nic', '   to m', '', 't you']
'''
'h'
'llo nic'
'   to m'
''
't you'
'''
# 如果没有设置切割符  默认以任意的空白符号为切割符  会将结果中的空字符串给移除
'''
空格
换行
制表符等等
'''
sub_list = s.split()
print(sub_list)  # ['hello', 'nice', 'to', 'meet', 'you']

# 设置切割次数
sub_list = s.split('e', 1)
print(sub_list)  # ['h', 'llo nice   to meet you']

sub_list = s.rsplit('e')
print(sub_list)  # ['h', 'llo nic', '   to m', '', 't you']

sub_list = s.rsplit('e', 1)
print(sub_list)  # ['hello nice   to me', 't you']

print("##------------------------")
sub_list = s.rsplit('e', 2)
print(sub_list)  # ['hello nice   to m', '', 't you']
sub_list = s.split('e', 4)
print(sub_list)  # ['h', 'llo nic', '   to m', '', 't you']
print("##------------------------")

# 2. 拼接
# 使用拼接符把序列中的内容拼接成一个字符串
'''
'拼接符'.join(序列)
	底层实现就是采用的+号拼接  【字符串只能跟字符串拼接】
	序列中的元素必须是字符串类型的

'''
words = ['hello', 'nice', 'to', 'meet', 'you']
res = '_'.join(words)
print(res)  # hello_nice_to_meet_you

# nums = (11, 23, 45)
# res = '+'.join(nums)  # TypeError: sequence item 0: expected str instance, int found