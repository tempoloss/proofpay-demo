import tinycalc


def test_add() -> None:
    assert tinycalc.add(2, 3) == 5


def test_subtract() -> None:
    assert tinycalc.subtract(5, 2) == 3


def test_multiply() -> None:
    assert tinycalc.multiply(4, 3) == 12


def test_divide() -> None:
    assert tinycalc.divide(6, 3) == 2
