import random

player = input("请输入石头（0）剪刀 （1）布 (2):")
player = int(player)
# randint 随机出 0 1 2 三个数的其中一个
computer = random.randint(0, 2)
# 可以在这里补充一些判断
computerZhao = ""
if computer == 0:
    computerZhao = "石头"
if computer == 1:
    computerZhao = "剪刀"
if computer == 2:
    computerZhao = "布"

print("计算机出了%s"%computerZhao)

# 玩法： 此处可以升级，大战300回合，看输赢的次数
if ((player == 0 and computer == 1)
        or (player == 1 and computer == 2)
        or (player == 2 and computer == 0)):
    print("玩家赢！！")
elif player == computer:
    print("平手，再来一局")
else:
    print("你输了，计算机赢了！")
