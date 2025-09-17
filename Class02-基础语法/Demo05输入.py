# 在input之前不是说必须打印，而是提示而已，不想要也无所谓
print("请输入你的密码：")
# input 会阻塞程序，如果不输入，不能进行下一步！
password = input()
print("请输入你的取款金额：")
money = input()
#money2 = "2389"
print(type(money))  # <class 'str'>
# input() 获取的数据都是 字符串类型
print("本次取款金额为"+money+"元")

#---------------------------------
#练习
print("请输入你的名字:")
name = input()
qq = "89923482"
phone = "18623894289"
compAddress = "北京市xxxx大街"
print("==============================")
print("姓名：%s"%name)
print("qq：%s"%qq)
print("手机号：%s"%phone)
print("compAddress：%s"%compAddress)
print("==============================")

#---------------------------------
name = "老闫"
age = 59
address = "宇宙第一大街101号"
phone = "18638147931"  #能量号
print("*"*30)
print("* 姓名：%s%20s"%(name,"*"))
print("* 手机号："+phone)
print("* 年龄："+str(age))
print("* 通讯地址："+address)
print("*"*30)

print("请输入您的尊姓大名：")
name2 = input()
phone2 = input("请输入您的手机号：")
address2 = input("贵府地址：")

print("*"*30)
print("* 姓名：%s%18s"%(name2,"*"))
print("* 手机号："+phone2)
print("* 通讯地址："+address2)
print("*"*30)