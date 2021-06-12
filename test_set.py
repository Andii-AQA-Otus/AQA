import pytest

def test_assert():
    set_1 = set('Hello world')
    set_2 = set('Hi world')
    assert set_1 is not set_2


@pytest.mark.parametrize("test_data", [5, 5, 5])
def test_add_2_set(set_fixture, test_data):
    a = set(set_fixture)
    a.add(test_data)
    assert len(a) == len(a)


def test_clear(set_fixture):
    a = set(set_fixture)
    a.clear()
    assert len(a) == 0


@pytest.mark.parametrize("test_data", [[11, 12, 13]])
def test_isdisjoint(test_data):
    s = [115, 152, 132, 113, 134]
    s1 = set(s)
    ch = set(test_data)
    assert s1.isdisjoint(ch)


def test_copy(set_fixture):
    s = set(set_fixture)
    s_copy = s.copy()
    assert s == s_copy