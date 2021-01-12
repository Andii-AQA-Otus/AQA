import pytest


def test_concatenation(first = "Hello", second = " ", third = "world!"):
    a = first
    b = second
    c = third
    assert "Hello world!" == a + b + c


def test_len(fixture_string):
    result = len(fixture_string)
    assert result == 11

def test_string_is_lower(fixture_str_lower):
    assert fixture_str_lower.islower()

def test_string_is_upper(fixture_string):
    assert fixture_string.isupper()

def test_string_capitalize(fixture_str_lower):
    assert fixture_str_lower.capitalize() == "Lower"