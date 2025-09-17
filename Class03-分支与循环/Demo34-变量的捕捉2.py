#  石头剪刀布，一局定生死
import random


def showQuan(num):
    match num:
        case 0:
            return "石头"
        case 1:
            return "布"
        case 2:
            return "剪刀"


print("余也请出拳.....")
a = int(input("[0 石头 1 布 2 剪刀]："))
print("机器人开始出拳.......")
b = int(random.randint(0, 2))
print("余爷出了：" + showQuan(a))
print("机器人出了：" + showQuan(b))

if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
    print("余也胜出，余也请自裁")
elif (a == b):
    print("平局，余也请自裁")
else:
    print("余也输了，请自裁.....")
print(str(a) + showQuan(a), str(b) + showQuan(b))
