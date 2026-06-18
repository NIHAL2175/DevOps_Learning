from calculator import ScientificCalculator
import pytest

calc = ScientificCalculator()

# ADDITION (5)

def test_add_1():
    assert calc.add(2, 3) == 5

def test_add_2():
    assert calc.add(-2, 2) == 0

def test_add_3():
    assert calc.add(0, 0) == 0

def test_add_4():
    assert calc.add(100, 200) == 300

def test_add_5():
    assert calc.add(-5, -5) == -10


# SUBTRACTION (5)

def test_sub_1():
    assert calc.subtract(10, 5) == 5

def test_sub_2():
    assert calc.subtract(5, 10) == -5

def test_sub_3():
    assert calc.subtract(0, 0) == 0

def test_sub_4():
    assert calc.subtract(-5, -5) == 0

def test_sub_5():
    assert calc.subtract(100, 50) == 50


# MULTIPLICATION (5)

def test_mul_1():
    assert calc.multiply(2, 3) == 6

def test_mul_2():
    assert calc.multiply(0, 10) == 0

def test_mul_3():
    assert calc.multiply(-2, 3) == -6

def test_mul_4():
    assert calc.multiply(-2, -3) == 6

def test_mul_5():
    assert calc.multiply(10, 10) == 100


# DIVISION (5)

def test_div_1():
    assert calc.divide(10, 2) == 5

def test_div_2():
    assert calc.divide(9, 3) == 3

def test_div_3():
    assert calc.divide(-10, 2) == -5

def test_div_4():
    assert calc.divide(-10, -2) == 5

def test_div_5():
    with pytest.raises(ValueError):
        calc.divide(10, 0)


# POWER (5)

def test_power_1():
    assert calc.power(2, 3) == 8

def test_power_2():
    assert calc.power(5, 2) == 25

def test_power_3():
    assert calc.power(10, 0) == 1

def test_power_4():
    assert calc.power(3, 1) == 3

def test_power_5():
    assert calc.power(2, 5) == 32


# SQUARE ROOT (5)

def test_sqrt_1():
    assert calc.square_root(25) == 5

def test_sqrt_2():
    assert calc.square_root(100) == 10

def test_sqrt_3():
    assert calc.square_root(0) == 0

def test_sqrt_4():
    assert calc.square_root(1) == 1

def test_sqrt_5():
    with pytest.raises(ValueError):
        calc.square_root(-1)


# FACTORIAL (5)

def test_fact_1():
    assert calc.factorial(0) == 1

def test_fact_2():
    assert calc.factorial(1) == 1

def test_fact_3():
    assert calc.factorial(5) == 120

def test_fact_4():
    assert calc.factorial(6) == 720

def test_fact_5():
    with pytest.raises(ValueError):
        calc.factorial(-1)


# MODULUS (5)

def test_mod_1():
    assert calc.modulus(10, 3) == 1

def test_mod_2():
    assert calc.modulus(20, 5) == 0

def test_mod_3():
    assert calc.modulus(7, 2) == 1

def test_mod_4():
    assert calc.modulus(15, 4) == 3

def test_mod_5():
    assert calc.modulus(100, 10) == 0


# ABSOLUTE VALUE (5)

def test_abs_1():
    assert calc.absolute(-10) == 10

def test_abs_2():
    assert calc.absolute(10) == 10

def test_abs_3():
    assert calc.absolute(0) == 0

def test_abs_4():
    assert calc.absolute(-999) == 999

def test_abs_5():
    assert calc.absolute(555) == 555


# PERCENTAGE (5)

def test_percent_1():
    assert calc.percentage(50, 100) == 50

def test_percent_2():
    assert calc.percentage(25, 100) == 25

def test_percent_3():
    assert calc.percentage(10, 20) == 50

def test_percent_4():
    assert calc.percentage(5, 10) == 50

def test_percent_5():
    with pytest.raises(ValueError):
        calc.percentage(10, 0)