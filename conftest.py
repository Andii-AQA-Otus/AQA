#Here are fixtures
import pytest



@pytest.fixture(params=[[11, 12, 12, 13, 14]])
def set_fixture(request):
    return request.param
  

@pytest.fixture(params=['HELLO WORLD'])
def fixture_string(request):
    return request.param

@pytest.fixture(params=['lower'])
def fixture_str_lower(request):
    return request.param



@pytest.fixture(params=[11, 12, 13, 14])
def list_params_fixture(request):
    return request.param

@pytest.fixture()
def get_list_fixture():
    return [1, 2, 3, 4]



@pytest.fixture()
def get_dictionary_fixture():
    return {'a': 1,'b': 2,'e': 5,'c': 3, 'd': 4}

@pytest.fixture(params=[{'t': 6}, {'t': 7}, {'t': 8}])
def dictionary_params_fixture(request):
    return request.param
