


def aaaa():
    print("请输入你猜想的字符：")
    a=input()
    if a=='3':
        print("哇哦，你猜对了")
        return "ok"
    else:
        print("你猜错了哦~~")
        return "fail"


for s in range(5):
    rsp = aaaa()
    if rsp=='ok':
        break










