import pytest

from square_mod import is_perfect_square_fixed as is_perfect_square

@pytest.mark.parametrize("n", [0, 1, 4, 9, 16, 25, 36] )
def test_squares(n):
    assert is_perfect_square(n)


@pytest.mark.parametrize("n", [2, 3, 5, 6, 7, 8, 27, 32])
def test_non_squares(n):
    assert not is_perfect_square(n)

@pytest.mark.xfail(strict=True)
def test_negative():
    assert not is_perfect_square(-4)
