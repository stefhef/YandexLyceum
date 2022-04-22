import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars('') == {}


def test_common_lower():
    assert count_chars('aaabbdd') == {'a': 3, 'b': 2, 'd': 2}


def test_common_other_case():
    assert count_chars('aaaBbddC') == {'a': 3, 'b': 1, 'd': 2, 'B': 1, 'C': 1}


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)
