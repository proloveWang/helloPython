# 索引
# python索引分为正向索引和负向索引
# ● 正向索引的范围是[0, 长度N - 1] 从左向右
# ● 负向索引的范围是[-1, -长度N] 从右向左
# 通过索引定位到对应位置，修改或者获取该位置的元素

nums = [19, 27, 38, 41, 25]

# 获取第2个元素
ele = nums[1]
print(ele)

# 获取倒数第二个
ele = nums[-2]
print(ele)

# 修改
nums[0] = 87
print(nums)  # [87, 27, 38, 41, 25]

nums[-1] = 65
print(nums)  # [87, 27, 38, 41, 65]






# 切片
# 切片类似于字符串 列表[start:stop:step]
# ● 正向切片步长step为正数 表示从左向右取值
# ● 负向切片步长step为负数 表示从右向左取值
# start和stop只是来定位取数据的范围
# ● start省略 正向切片的时候 表示从最左边开始 负向切片表示从最右边开始
# ● stop省略 正向切片的时候 表示到最右边结束 负向切片表示到最左边结束


# 切片
sun_nums = nums[::2]
print(sun_nums)  # [87, 38, 65]

sun_nums = nums[::-1]
print(sun_nums)  # [65, 41, 38, 27, 87]

sun_nums = nums[:]
print(sun_nums)  # [87, 27, 38, 41, 65]  备份了一份

'''
切片：根据索引以及步长定位到列表的多个位置
因为列表是可变的  也可以通过切片对这些位置的数据进行修改  【赋值得是一个序列型数据】
切片定位的下标范围是连续的  赋值的个数可以随便
但是位置是跳跃的  定位到几个位置  就得赋予几个值
'''
print("print(nums) ")
print(nums)
nums[:2] = [19, 33]
print(nums)  # [19, 33, 38, 41, 65]
nums[:2] = [19]
print(nums)  # [19, 38, 41, 65]
nums[:2] = [19, 99, 78, 36]
print(nums)  # [19, 99, 78, 36, 41, 65]

# nums[::2] = [99]
# print(nums)  # ValueError: attempt to assign sequence of size 1 to extended slice of size 3

nums[::2] = [99] * 3
print(nums)  # [99, 99, 99, 36, 99, 65]











