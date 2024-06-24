import pytest
import source.shapes as shapes


def test_area(my_rectangle):
    assert my_rectangle.area() == 20 * 10


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (20 + 10)


def test_not_equal(my_rectangle, my_rectangle2):
    assert my_rectangle != my_rectangle2
