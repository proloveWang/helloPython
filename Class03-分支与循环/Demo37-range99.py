# 使用range 将99乘法表 改造
for m in range(1,10):
    for n in range(1,10):
        if n <= m:
            print("%d*%d=%-2d"%(n,m,(m*n)), end=" ")
    print()