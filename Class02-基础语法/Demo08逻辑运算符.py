'''
and	逻辑与，连接的表达式之间是并且的关系，也就是需要两个表达式同时成立，结果才是成立的，有一句总结是 一假则全假根据总结，逻辑与有短路原则：左边表达式为假，右边表达式不参与运算这个短路只针对与and有效，后面有其他的逻辑表达式还是会执行的	False and False = FalseFalse and True = FalseTrue and False = FalseTrue and True = True
or	逻辑或，连接的表达式之间是或者的关系，也就是其中一个表达式成立，结果就是成立的，有一句总结是 一真则全真根据总结，逻辑或有短路原则：左边表达式为真，右边表达式不参与运算这个短路是真短路，后面所有的表达式都不会执行了	False or False = FalseFalse or True = TrueTrue or False = TrueTrue or True = True
not	逻辑非，对逻辑结果取反的，真变假，假变真优先级别比and和or高	not False = True  not True = False
'''
# 逻辑运算符 --> 使用逻辑运算符列出逻辑表达式
age = 15
number = 95
ch = 'x'
a,b,c = 1,2,3
year = 2025
# 1:参加少年运动会的运动员的年龄在13～17之间）
age >= 13 and  age <= 17

# 2:（动物园年龄小于12，大于65的老人免票）
age < 12 or age > 65

# 3:（年龄不小于16岁的人才可以观影）
not age < 16 or age >= 16

# 4:构造一个表达式来表示下列条件：
# a:number等于或大于90，但小于100
number >= 90 and number < 100
# b:ch不是字符q也不是字符k
ch != 'q' and ch != k
# c:number界于1到9之间（包括1不包括9），但是不等于5
(number >= 1 and number < 9) and number != 5
# d:number不在1到9之间
number < 1 or number > 9
not (number>=1 and number<=9)

# 5:判断这个字符是空格，是数字，是字母
ch == ' '
ch >= '0' and ch <= '9'
(ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')

# 6:有3个整数a,b,c，判断谁最大，列出所有可能
a > b and a > c
b > a and b > c
c > a and c > b
# 7:判断year表示的某一年是否为闰年，用逻辑表达式表示。闰年的条件是符合下面二者之一：a:能被4整除但不能被100整除 b:能被400整除
(year%4==0 and year%100!=0) or (year%400==0)