#  除法结果是小数
print(7 / 2)
# 整除 //
print(7 // 3)
# 取模 求余数
print(7 % 3)
# 一个数的几次方 **
print(2 ** 3)

# 一下赋值两个变量
a, b = 10, 20
c = 10 + 20 * 4

# 赋值可以赋值不同类型的，打印可以同时打印多个值
name, age = "zhangsan", 20
print(name, age)

# 海象运算法  python3.8之后的新特性
# 没有使用这个运算法的写法：
# start = input("Do you want to start(y/n)?")
# print(start == "y")

# 语法糖 语法中的调味料
# print(start := input("Do you want to start(y/n)?") == 'n')

# 比较运算法
str1 = 'a'
str2 = 'a'
print(str1 == str2)
print(str1.__eq__(str2))  # __eq__ 作为字符串比较的话，比较的是字符串的值，不是比较的地址

# python允许在进行范围比较的时候，使用连续比较的方式
score = 90
print(60 <= score <= 100)

# 将两个输入的值进行相加
num01 = int(input("请输入第一个值："))
num02 = int(input("请输入第二个值："))
# 只有字符串和字符串之间才可以进行+号拼接
print("两个值之和为"+str(num01 + num02))

a = int(3.14)
print(a)
# 这个写法是错误的，将字符串变为int,里面的内容必须是可以转化为int的字符串
# b = int("3.14")
b = int("3")
print(b)

# bool 里面只要不是空的，或者不是0 就都返回True
print(bool(1))
print(bool(0))   # False
print(bool("0"))
print(bool(None))  # False