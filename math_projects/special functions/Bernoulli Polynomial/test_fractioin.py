from fractions import Fraction


def is_rational(num):
    fraction = Fraction(num).limit_denominator()
    return fraction.denominator != 1  # 如果分母为1，则表示是整数（有理数）


# 示例
num = 3.5
print(f"{num} 是有理数吗？{is_rational(num)}")
