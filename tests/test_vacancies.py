import pytest
from src.vacancies import Vacancy


@pytest.fixture
def test_vacancy():
    return Vacancy("python", 1)


def test_name_error(test_vacancy):
    """Проверка на наличии ошибок в названии вакансии"""
    with pytest.raises(AttributeError):
        test_vacancy.name = "something"


def test_page_error(test_vacancy):
    """Проверка на наличие ошибок при вводе количества"""
    with pytest.raises(AttributeError):
        test_vacancy.page = "something"


def test_str(test_vacancy):
    """Проверка метода str"""
    assert str(test_vacancy) == "python"


def test_repr(test_vacancy):
    """Проверка метода repr"""
    assert repr(test_vacancy) == "Vacancy(('python', 1))"