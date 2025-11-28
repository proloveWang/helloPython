import random
class caisuziclass:
    def work(self):
        print("员工需要努力搬砖哦！")

    def generate_secret_number_2(guess_len_2):
        """生成一个4位不重复数字的字符串"""
        digits = list(range(10))
        random.shuffle(digits)
        return ''.join(str(d) for d in digits[:guess_len_2])