from src.hh_errors_debug import HHRequestsDebug
from src.debug_users_json import DebugUsersJson
from src.sorted_vacancies import SortedVacancies
from hh_connection import GetHeadHunter


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
        search_result = GetHeadHunter(search_query, top_n)
        search_result.get_json()


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
        json_file = SortedVacancies()
        json_vacancies = json_file.hh_sorted_vacancies
        salary = self.user_input_int()
        city = self.user_input_str()

        for vacancy in json_vacancies:
            if salary > vacancy['min_salary']:
                continue
            if city == vacancy['city']:
                vacancies_list.append(vacancy)
            if city == '':
                vacancies_list.append(vacancy)

        for result in vacancies_list:
            print(f"Город: {result['city']}\nДата публикации: {result['date']}\n"
                  f"Должность: {result['name']}\nТребование: {result['requirement']}\n"
                  f"Ответственность: {result['responsibility']}\nЗарплата от {result['min_salary']}\nЗарплата до {result['max_salary']}")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')


if __name__ == '__main__':
    r = UserInteractionHH()
    print(r.hh_user_search())
