# \n 就是换行的意思
print("2378472384723-------------------")
# ctrl + d  复制一行
print("2378472384723\n-------------------")
print("*", end="\n") # print 本身就自带换行的功能
print("#####  ",end="") # print不换行
print("******")

print("Good Good Study ,'Day Day Up!'")
print('Good Good Study ,"Day Day Up!"')
# 输出结果：
# Good Good Study ,'Day Day Up!'
# Good Good Study ,"Day Day Up!"
# 单引号中不能再单引号，双引号中不能再加双引号

# "" 和 '' 本身是标识一个字符串的意思，但是现在呢想修改它原本的意思，加 \ ,就叫做转义
print("我的爱好是学习\"Python\"")
print('我的爱好是学习\'Python\'')

# 三引号除了有注释的功能外，还有换行的功能
print("""
     卜算子咏梅
          我也不知道，你也不知道，
     大家都不知道，哇，好诗！
""")
# 输出的结果：
#      卜算子咏梅
#           我也不知道，你也不知道，
#      大家都不知道，哇，好诗！

# 这种写法不换行
print("hello"
      "world")
# 这种写法才换行！
print("hello\n"
      "world")

name = "闫哥"
qq = "89923482"
phone = "18623894289"
compAddress = "北京市xxxx大街"
print("==============================")
print("姓名：%s"%name)
print("qq：%s"%qq)
print("手机号：%s"%phone)
print("compAddress：%s"%compAddress)
print("==============================")