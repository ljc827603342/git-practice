# 简单计算器程序


def 加法(数字1, 数字2):
    """返回两个数字的和"""
    return 数字1 + 数字2


def 减法(数字1, 数字2):
    """返回两个数字的差"""
    return 数字1 - 数字2


def 乘法(数字1, 数字2):
    """返回两个数字的积"""
    return 数字1 * 数字2


def 除法(数字1, 数字2):
    """返回两个数字的商"""
    if 数字2 == 0:
        return "错误：除数不能为零"
    return 数字1 / 数字2


def 显示菜单():
    """显示计算器菜单"""
    print("=" * 30)
    print("    简易计算器")
    print("=" * 30)
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("0. 退出")
    print("-" * 30)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        from decimal import Decimal, DivisionByZero
        return float(Decimal(str(a)) / Decimal(str(b)))
    return "除数不能为零！"

if __name__ == "__main__":
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

if __name__ == "__main__":
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")

if __name__ == "__main__":
    while True:
        显示菜单()
        选择 = input("请输入你的选择：")

        if 选择 == "0":
            print("感谢使用，再见！")
            break

        if 选择 not in ("1", "2", "3", "4"):
            print("无效选择，请重新输入")
            continue

        数字1 = float(input("请输入第一个数字："))
        数字2 = float(input("请输入第二个数字："))

        if 选择 == "1":
            结果 = 加法(数字1, 数字2)
            print(f"{数字1} + {数字2} = {结果}")
        elif 选择 == "2":
            结果 = 减法(数字1, 数字2)
            print(f"{数字1} - {数字2} = {结果}")
        elif 选择 == "3":
            结果 = 乘法(数字1, 数字2)
            print(f"{数字1} * {数字2} = {结果}")
        elif 选择 == "4":
            结果 = 除法(数字1, 数字2)
            print(f"{数字1} / {数字2} = {结果}")

        print()
