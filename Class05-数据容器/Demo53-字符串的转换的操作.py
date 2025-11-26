s = 'helLo,Nice to Meet you.My age is 18.aheklfnfsd hjdhsjhgfs '

# 1. 将小写英文字母转化为大写 其他的不变
new_s = s.upper()
print(new_s)  # HELLO,NICE TO MEET YOU.MY AGE IS 18.
print(s)

# 2. 将大写英文字母转化为小写 其他的不变
new_s = s.lower()
print(new_s)  # hello,nice to meet you.my age is 18.

# 3. 大写转小写 小写转大写 其他字符不变
new_s = s.swapcase()
print(new_s)  # HELLO,nICE TO mEET YOU.mY AGE IS 18.

# 4. 首字母大写 其他字母小写  其他符号不变
new_s = s.capitalize()
print(new_s)  # Hello,nice to meet you.my age is 18.

# 5. 每个单词首字母大写 其他小写
# 单词: 非连续性的符号组在一起就是单词
new_s = s.title()
print(new_s)  # Hello,Nice To Meet You.My Age Is 18.Aheklfnfsd Hjdhsjhgfs



