
#
#
# def aaaa():
#     print("请输入你猜想的字符：")
#     a=input()
#     if a=='3':
#         print("哇哦，你猜对了")
#         return "ok"
#     else:
#         print("你猜错了哦~~")
#         return "fail"
#
#
# for s in range(5):
#     rsp = aaaa()
#     if rsp=='ok':
#         break
#
#

# 5.9. 容器综合案例
import random
def getRandomBalls():
    list01 = list()
    while len(list01) < 6:
        num = random.randint(1, 33)
        if num not in list01:
            list01.append(num)
    lanNum = random.randint(1, 16)
    list01.append(lanNum)
    return list01

print(getRandomBalls())

print(random.randint(10, 99))
print(random.randint(10, 99))
print(random.randint(10, 99))
print(random.randint(10, 99))
print(random.randint(10, 99))
print(random.randint(10, 99))

lanNum = random.randint(10, 99)
print("请输入一个数字")
while True:
    youInput = input()
    youInput=int(youInput)
    if youInput>lanNum:
        print("数值太大了，重新输入吧~~~~")
    elif youInput<lanNum:
        print("数值太小了，重新输入吧~~~~")
    else:
        print("哇哦，你猜对了")
        break



