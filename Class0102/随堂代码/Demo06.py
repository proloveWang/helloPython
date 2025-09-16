"""
 石头剪 0  刀   1   布  2
 两个人： 你是输入的值，计算机是随机的值
"""
import random

print(random.randint(0, 2))

"""
   思路：
      先获取玩家的输入的值
      再获取计算机随机出来的值
      再根据这两个值进行条件判断
"""
# 先获取玩家的输入的值
playerNum = int(input("请输入您想要出的数字："))

computerNum = random.randint(0, 2)
print("玩家出的是：%d" % playerNum)
print("计算机出的是：%d" % computerNum)
if (playerNum == 0 and computerNum == 1) or (playerNum == 1 and computerNum == 2) or (
		playerNum == 2 and computerNum == 0):
	print("你赢了！")
elif playerNum == computerNum:
	print("打平了")
else:
	print("你输了！")
