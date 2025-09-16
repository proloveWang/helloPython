# 基础语法
# match 变量:
#     case 字面量1:
#         如果变量的值等于字面量1，执行这里的业务逻辑
#     case 字面量2:
#         如果变量的值等于字面量2，执行这里的业务逻辑
#     ...
#     case _:
#         如果变量的值，与上面的每一个case的字面量都不一样，执行这里的业务逻辑
#
# 案例:
# 从控制台输入一个数字，根据数字输出对应的季节
# 1 => spring, 2 => summer, 3 => autumn, 4 => winter，如果是其他数字，输出other
# 变量的捕捉
# match 变量:
#     case 字面量1:
#         如果变量的值等于字面量1，执行这里的业务逻辑
#     case 变量2:
#         如果变量的值与字面量1没有匹配上，就会将变量的值赋值给变量2！
#

season = int(input("please input a season number: "))
match season:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autumn")
    case 4:
        print("winter")
    case other:
        print(f"wrong season: {other}")
        print(other)
# 注意事项：如果在输入的时候，输入的是1-4的数字，可以被case捕获到，就不会创建other变量，这里就会出问题


"""
情节描述：上公交⻋，并且可以有座位坐下
要求：输⼊公交卡当前的余额，只要超过2元，就可以上公交⻋；如果空座位的数量⼤于0，就可以坐下
"""
yueE = 1
seatNum = 3
if yueE >= 2:
    if seatNum > 0:
        print("有座位，请入座")
    else:
        print("没座位，站着")
else:
    print("余额不足，欢迎下次光临！")