from main import Calculator
thing = Calculator(100, 10)
thing1 = Calculator(100, 0)


def test_minus_num():
    assert thing.minus_num() == 90
def test_plus_num():
    assert thing.plus_num() == 110
def test_multiply_by_num():
    assert thing.multiply_by_num() == 1000
def test_devide_by_num():
    assert thing.divide_by_num() != 19
def test_devide_by_zero():
    assert thing1.divide_by_num() == "cant devide by zero"
def test_to_number_power():
    assert thing.to_number_power() != 90000000000
def test_get_remainder():
    assert thing.get_remainder() == 0