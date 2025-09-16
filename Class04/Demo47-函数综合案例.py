# 函数综合案例
# 综合练习 万年历
# 需求:
# 1.先输出提示语句,并接受用户输入的年,月
# 2.根据用户输入的年,先判断是否是闰年
# 3.根据用户输入的月来判断月的天数
# 4.用循环计算用户输入的年份距离1900年1月1日的总天数
# 5.用循环计算用户输入的月份距输入的年份的1月1日共有多少天
# 6.相加第4步与第5步的天数,得到总天数,
# 7.用(总天数+1)%67来计算输入的月的第一的星期数
# 8.根据第7步得到的值,格式化输出这个月的日历
# 样式:
# 请输入年:
# 2018
# 清输入月:
# 3
# 星期日  星期一  星期二 星期三  星期四  星期五  星期六
# 说明:
# 第4步需要注意的是1900年距离当前年份的总天数,当前年份还没有过完,所以不能算当前年份
# 第5步计算的是当前月距离当前年份1月1日的天数,也就是计算月份天数的和
# 第7步(总天数+1)%7这个公式得到的结果是0~6中的某一个,那么这里0就是星期天依次类推

# 提示语句  年 月
# 判断是否为闰年的
def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# 给定月份，算出来该月份有几天
def getDayOfMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if isLeapYear(year):
            return 29
        else:
            return 28


run = 2
while True and run > 0:
    run -= run
    yearStr = input("请输入年份（数字）:")
    if yearStr.isdigit():
        year = int(yearStr)
        monthStr = input("请输入月份（1-12）:")
        if monthStr.isdigit() and 1 <= int(monthStr) <= 12:
            month = int(monthStr)
            # 计算该年月距离 1900-01-01的总天数
            totalDays = 0
            for y in range(1900, year):
                if isLeapYear(y):
                    totalDays += 366
                else:
                    totalDays += 365
            # 将剩余月份的天数相加
            for m in range(1, month):
                totalDays += getDayOfMonth(year, m)

            print(totalDays)
            # 该年该月的第一天是星期几
            firstDayOfMonth = (totalDays + 1) % 7
            print(firstDayOfMonth)
            # 接着进行格式化输出
            print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t")
            # 规律 星期几就打印几个空格
            # 一个tab 两个汉字
            # print("\t"*2)
            counter = firstDayOfMonth
            print("\t" * 2 * firstDayOfMonth, end="")
            # 打印几号
            dayOfMonth = getDayOfMonth(year, month)
            for day in range(1, dayOfMonth + 1):
                print(day, end="\t\t")
                counter += 1
                # 控制换行，没打印7个值包括空白都换行
                if counter % 7 == 0:
                    print()
            print()

        else:
            print("输入的数据不合法，请输入1~12之间的数字")
    else:
        print("请输入数字，不要闹")
