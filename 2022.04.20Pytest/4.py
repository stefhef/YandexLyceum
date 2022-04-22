import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_its_position():
    assert is_under_queen_attack('a1', 'a1')


def test_impossible_position():
    assert not is_under_queen_attack('a1', 'b8')


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack('a5', 42)


def test_wrong_coordinates_1():
    with pytest.raises(ValueError):
        is_under_queen_attack('aa1', 'b2')


def test_wrong_coordinates_2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a1', 'aa2')


def test_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack('a1', 'a10')


def test_attack_same_row():
    assert is_under_queen_attack('a1', 'e1')


def test_attack_same_column():
    assert is_under_queen_attack('a1', 'a8')


def test_attack_same_diagonal_1():
    assert is_under_queen_attack('a1', 'h8')


def test_attack_same_diagonal_2():
    assert is_under_queen_attack('a8', 'h1')
