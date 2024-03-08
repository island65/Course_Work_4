from src.hh_errors_debug import HHRequestsDebug
from src.debug_users_json import DebugUsersJson
from src.vacancy_class import Vacancy
from src.hh_connection import GetHeadHunter
from src.utils import read_data
from src.json_saver import JsonSaver


class UserInteractionHH(HHRequestsDebug):
    """
    Класс для обращения пользователя к сайту hh.ru
    """
    def hh_user_search(self):
        """
        Метод для ввода данных для поиска вакансий на hh.ru
        """
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        hh = GetHeadHunter(search_query, top_n)
        vacancies = hh.get_vacancy
        sorted_vacancies = Vacancy.hh_data_validation(vacancies)
        json_saver = JsonSaver()
        json_saver.write_data_json(sorted_vacancies)


class UserInteractionJson(DebugUsersJson):
    """
    Класс взаимодействия пользователя с файлом json
    """
    def json_user_search(self):
        """
        Метод сортировки вакансий json файла
        :return:
        """
        vacancies_list = []
        json_file = read_data()
        salary = self.user_input_int()
        city = self.user_input_str()

        for vacancy in json_file:
            if salary > vacancy['min_salary']:
                continue
            if city == vacancy['city']:
                vacancies_list.append(Vacancy(**vacancy))
            if city == '':
                vacancies_list.append(Vacancy(**vacancy))

        for result in vacancies_list:
            print(result)
        if len(vacancies_list) == 0:
            print(f'Результатов 0')
