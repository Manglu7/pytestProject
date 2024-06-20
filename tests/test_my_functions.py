import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 2)
    assert result == 3


def test_divide():
    result = my_functions.divide(2, 2)
    assert result == 1


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)