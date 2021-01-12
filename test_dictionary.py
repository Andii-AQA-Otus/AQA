import pytest

def test_dictionary_2_pop(get_dictionary_fixture):
    dict= get_dictionary_fixture
    result = dict.pop('c')
    assert result == 3

def test_dictionary_1_keys(get_dictionary_fixture):
    dict = get_dictionary_fixture
    sorted(dict.keys())
    assert dict['e'] == 5


def test_update_dictionary(get_dictionary_fixture):
    dict1 = get_dictionary_fixture
    dict2 = {'f': 6}
    dict1.update(dict2)
    result = dict1['f']
    assert result == 6


def test_dictionary_for_get(get_dictionary_fixture):
    dict = get_dictionary_fixture
    result = dict.get('a')
    assert result == 1


def test_dictionary_5_del_params(get_dictionary_fixture, dictionary_params_fixture):
    data = [6, 7, 8]
    dict1 = get_dictionary_fixture
    dict2 = dictionary_params_fixture
    dict1.update(dict2)
    result = dict2.get('t')
    success = False
    for num in data:
        if num == result:
            success = True
    assert success