import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''


def test_single_char():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('323') == '323'


def test_common():
    assert reverse('123') == '321'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type_iterable():
    with pytest.raises(TypeError):
        reverse(['a', '2', '3'])

