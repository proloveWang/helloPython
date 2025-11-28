import random

from MyTest.caisuziclass import caisuziclass

guess_len = 2

def generate_secret_number(guess_len_2):
    """生成一个4位不重复数字的字符串"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(str(d) for d in digits[:guess_len_2])


def check_guess(secret, guess):
    """检查猜测结果，返回A和B的数量"""
    a_count = 0  # 位置和数字都正确
    b_count = 0  # 数字正确但位置错误

    # 检查A（位置和数字都正确）
    for i in range(guess_len):
        if guess[i] == secret[i]:
            a_count += 1

    # 检查B（数字正确但位置错误）
    secret_digits = list(secret)
    guess_digits = list(guess)

    # 先排除已经匹配的位置
    temp_secret = []
    temp_guess = []

    for i in range(guess_len):
        if guess[i] != secret[i]:
            temp_secret.append(secret[i])
            temp_guess.append(guess[i])

    # 计算B的数量
    for digit in temp_guess:
        if digit in temp_secret:
            b_count += 1
            temp_secret.remove(digit)

    return a_count, b_count


def main():

    print("欢迎来到数字猜谜游戏！")
    print("规则：")
    print("- 我生成了一个4位不重复的数字")
    print("- 如果数字和位置都正确，记为A")
    print("- 如果数字正确但位置错误，记为B")
    print("- 例如：答案1234，输入1567记为1A0B，输入2789记为0A1B")
    print("- 输入'quit'可以退出游戏")
    print("- 本次生成的数字是%s位数字" % (guess_len))
    print()



    # secret_number = generate_secret_number(guess_len)
    secret_number = caisuziclass.generate_secret_number_2(guess_len)
    print(secret_number)
    attempts = 0

    print("游戏开始！请输入你的猜测：")

    while True:
        guess = input(f"第{attempts + 1}次尝试: ").strip()

        # 检查退出条件
        if guess.lower() == 'quit':
            print(f"游戏结束！正确答案是: {secret_number}")
            break

        # 验证输入格式
        if len(guess) != guess_len or not guess.isdigit():
            print("请输入%s位数字！"%(guess_len))
            continue

        # 检查是否有重复数字
        if len(set(guess)) != guess_len:
            print("请输入%s个不重复的数字！"%(guess_len))
            continue

        attempts += 1

        # 检查猜测结果
        a_count, b_count = check_guess(secret_number, guess)

        # 显示结果
        print(f"结果: {a_count}A{b_count}B")

        # 检查是否猜中
        if a_count == guess_len:
            print(f"恭喜你！在第{attempts}次尝试中猜对了数字！")
            break


if __name__ == "__main__":
    main()