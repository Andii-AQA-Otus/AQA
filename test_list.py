import pytest

def test_list_remove(get_list_fixture):
    l = get_list_fixture
    l.remove(3)
    result = True
    for num in l:
        if result:
            result = (num == 3)
    assert not result


def test_list_append(get_list_fixture):
    l = get_list_fixture
    l.append(11)
    result = False
    for num in l:
        if not result:
            result = (num == 11)
    assert result


def test_list_pop(get_list_fixture):
    l = get_list_fixture
    l.pop(3)
    result = True
    for num in l:
        if result:
            result = (num == 4)
    assert not result


def test_list_for_extend(get_list_fixture):
    l1 = get_list_fixture
    l2 = [10, 20, 30]
    l1.extend(l2)
    assert l1[5] == 20


def test_list_insert_5_params(get_list_fixture, list_params_fixture):
    l1 = get_list_fixture
    l2 = list_params_fixture
    l1.insert(0, l2)
    assert l1[0] == l2
