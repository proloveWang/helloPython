# for 临时变量 in 列表或者字符串等:
#   循环满⾜条件时执⾏的代码
# else:
#   循环不满⾜条件时执⾏的代码


#-------------------
name = "laoYan"
# x 其实就是变量，每一次从name这个字符串中获取一个字符
# 赋值给 x
for x in name:
    print(x)
#-------------------
print("-------------------")
#-------------------
name = ''
for x in name:
    print("x="+x)
else:
    print("没有数据")
#-------------------
print("-------------------")
#-------------------
# break/continue只能⽤在循环中，除此以外不能单独使⽤
# break/continue在嵌套循环中，只对最近的⼀层循环起作⽤
#-------------------
# 需求：当打印到n 结束，循环结束
name = "yanGe"
for a in name:
    print(a)
    if a == 'n':
        # break 跳出整个循环
        break
#-------------------
print("-------------------")
#-------------------
# 需求：打印 yanGe ，不打印G 字符
name = "yanGe"
for b in name:
    if b == 'G':
        # continue 跳出本次循环
        continue
    print(b)











