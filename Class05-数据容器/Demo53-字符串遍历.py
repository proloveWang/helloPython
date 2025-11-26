# 字符串遍历
# 方式1：直接遍历获取元素
# for 变量名 in 字符串:
# 	操作
# 方式2：使用range生成下标数列，根据下标获取元素
# 方式3：enumerate枚举遍历序列
# 对序列操作完成时候 会生成一个新的序列，这个序列中的元素是一个二元组 (下标, 元素)

s = 'nice hello'

for ch in s:
    print(ch)
'''
n
i
c
e
'''
print('=' * 30)

# 因为字符串是有序序列 可以通过索引获取元素
for i in range(len(s)):
    print(i, s[i])

# 获取e这个字符在字符串中的位置
# 直接遍历下标
for i1 in range(len(s)):
    if s[i1] == 'e':
        print(i1)

print('=' * 40)

#  enumerate(s) ---> [(下标, 元素), (下标1, 元素1), (下标2, 元素2)] --》元组的操作在后面会详细说明 这里大家知道如何操作即可
for item in enumerate(s):
    print(item)
'''
(0, 'n')
(1, 'i')
(2, 'c')
(3, 'e')
(4, ' ')
(5, 'h')
(6, 'e')
(7, 'l')
(8, 'l')
(9, 'o')
'''
print("=================解包")
# 解包： 给多个变量赋值的时候
x, y, z = 10, 11, 12
print(x, y, z)  # 10 11 12
'''
当用逗号分割定义数据时， 解释器会将其解释为一个元组类型
'''
data = 1, 2, 3, 4, 5, 6  # 打包
print(data, type(data))  # (1, 2, 3, 4, 5, 6)  <class 'tuple'>
'''
当把多个数据赋值给多个变量时， 是在给元组数据解包， 将数据赋值给对等位置的变量
'''

print("=================for enumerate")
# s = 'nice hello'
for pos, ele in enumerate(s):
    if ele == 'e':
        print(pos)























