score =input("请输入学生的分数：")
score = int(score)
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("不及格")