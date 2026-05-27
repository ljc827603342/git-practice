import sys
sys.path.insert(0, "src")

import main


# ========== 中文函数测试 ==========

def test_加法_正数():
    assert main.加法(3, 4) == 7


def test_加法_负数():
    assert main.加法(-3, -4) == -7


def test_加法_零():
    assert main.加法(5, 0) == 5


def test_减法_正数():
    assert main.减法(10, 3) == 7


def test_减法_结果为负():
    assert main.减法(3, 10) == -7


def test_乘法_正数():
    assert main.乘法(3, 4) == 12


def test_乘法_零():
    assert main.乘法(5, 0) == 0


def test_除法_正常():
    assert main.除法(10, 2) == 5


def test_除法_除数为零():
    assert main.除法(5, 0) == "错误：除数不能为零"


# ========== 英文函数测试 ==========

def test_add():
    assert main.add(10, 5) == 15


def test_subtract():
    assert main.subtract(10, 5) == 5


def test_multiply():
    assert main.multiply(10, 5) == 50


def test_divide():
    assert main.divide(10, 5) == 2.0


def test_divide_by_zero():
    assert main.divide(10, 0) == "除数不能为零！"
