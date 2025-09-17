# 相同点：replaceAll 和 replace 都是全部替换
# 不同点：replaceAll支持正则表达式，因此会对参数进行解析（replaceAll的两个参数均是），如replaceAll(“\d”, ““)，而replace则不会。

mystr = 'hello world bigdata and bigdataNiu'
# 查找某个字符串是否在另一个字符串中，如果能查询到，就返回字符串最开始的位置的下标
# 6
print(mystr.find("world"))
# -1 表示没有找到
print(mystr.find("bigdata"))
# find 可以跟上查找的开始和结束的位置，如果不写，全部查找
print(mystr.find("world",10,20))
# index 查找某个字符串是否在另一个字符串中，作用跟find一样
# 6
print(mystr.index("world"))
# 找不到就报错：ValueError: substring not found
# print(mystr.index("world",10,20))

# count 某个字符串在另一个字符串中出现了几次
print(mystr.count("a")) # 5
# 如果没有出现，返回次数 0
print(mystr.count("laoYan")) # 0

# replace 替换的意思
newString = "hello hehe,You hehe ,I hehe"
# 全部替换
print(newString.replace("he","ha"))
# 指定次数替换
print(newString.replace("he","ha",3))

# split 切割的意思 ，切割出来是一个数组
print(newString.split(" ")) # ['hello', 'hehe,You', 'hehe', ',I', 'hehe']
# 2 表示切割几次
print(newString.split(" ",2)) # ['hello', 'hehe,You', 'hehe ,I hehe']

# capitalize  将首字母变大写
str = "hello world!"
print(str.capitalize())  #Hello world!
# title 把字符串的每个单词⾸字⺟⼤写
print(str.title()) # Hello World!

#startsWith 判断是否以某个单词开头，区分大小写
print(str.startswith("He")) # False
#endswith 判断是否以某个单词结尾，区分大小写
print(str.endswith("!"))  #True

#lower 将所有的大写变小写
print(str.lower()) #hello world!
#upper 将所有的小写变大写
print(str.upper()) #HELLO WORLD!

# ljust 返回⼀个原字符串左对⻬,并使⽤空格填充⾄⻓度 width 的新字符串
str = "hello"
print(str.ljust(10)) # "hello     "
print(str.rjust(10)) # "     hello"

# center 居中
print(str.center(11)) # "   hello   "

# strip 截取左边和右边的空白
# lstrip 截取左边 l = left
# rstrip 截取右边 r = right
str = "   nihaoya    "
print(str.strip()) #  "nihaoya"
print(str.lstrip()) # "nihaoya    "
print(str.rstrip()) # "   nihaoya"

# partition 部分的意思
# 方法的作用是将一个字符串切割为三部分
str = "bigdata laoyan spark!"
print(str.partition("laoyan")) # ('bigdata ', 'laoyan', ' spark!')
# 当子串不存在 就会出现如下的情况：
print(str.partition("laoli")) #('bigdata laoyan spark!', '', '')

# splitlines 按照⾏分隔，返回⼀个包含各⾏作为元素的列表
str = "hello \n world"
print(str.splitlines()) # ['hello ', ' world']
# isalpha 如果 mystr 所有字符都是字⺟ 则返回 True,否则返回 False
print(str.isalpha())
str = "helloworld"
print(str.isalpha()) # True

# isdigit 判断字符串中是否都是数字 如果是True
str = "19819281312"
print(str.isdigit()) # True

# isalnum  判断是否都是字母或者数字
str ="hello1234"
print(str.isalnum()) # True

# isspace 判断一个字符串是否为空白 不是null
str ="      "
print(str.isspace()) # True
# str = None
# 'NoneType' object has no attribute 'isspace'
# print(str.isspace())

# join mystr 中每个字符后⾯插⼊str,构造出⼀个新的字符串
str = "-"
arr = ["my","name","is","HanMeiMei"]
print(str.join(arr)) # my-name-is-HanMeiMei






#-------------------
print("-------------------")
#-------------------





