import pytest
from src.hh_connection import GetHeadHunter
from src.sorted_vacancies import SortedVacancies


@pytest.fixture
def test_head_hunter():
    return GetHeadHunter("python", 1)


def test_sorted_vacancy():
    r = SortedVacancies()
    assert r.hh_sorted == []
    assert r.date_format == None


def test_hh_sorted_vacancies():
    r = SortedVacancies()
    assert r.hh_sorted_vacancies == [{'city': 'Оренбург',
                                      'date': '29.01.2024',
                                      'max_salary': 50000,
                                      'min_salary': 50000,
                                      'name': 'Стажер-разработчик Python',
                                      'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть '
                                                     'активным и внедрять эффективные решения.',
                                      'responsibility': 'Внедрять новые инженерные решения. Поддерживать текущий '
                                                        'проект. Разработка десктоп ПО по нашим лекалам.'}]


def test_errors_vacancies_sorted():
    with pytest.raises(TypeError):
        SortedVacancies("python")