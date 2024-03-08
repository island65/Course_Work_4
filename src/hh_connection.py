from src.vacancyAPI import VacancyAPI
import requests


class GetHeadHunter(VacancyAPI):
    """
    Класс для получения вакансий с сайта hh.ru
    с наследованием от VacancyAPI, Vacancy
    """
    def __init__(self, name, top_n):
        """
        Создание экземпляра класса GetHeadHunter
        """
        self.__name = name
        self.__top_n = top_n
        self.url = "https://api.hh.ru"

    @property
    def name(self):
        """
        Геттер для приватного аттрибута name
        """
        return self.__name

    @property
    def top_n(self):
        """
        Геттер для приватного аттрибута top_n
        """
        return self.__top_n

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.top_n})"

    def get_request(self):
        """
        Метод чтения вакансий с HH.ru
        :return: json
        """
        response = requests.get(f"{self.url}/vacancies",
                                params={'text': self.name,
                                        'area': 113,
                                        'enable_snippets': "true",
                                        'only_with_salary': "true",
                                        'per_page': self.top_n})
        return response

    @property
    def get_vacancy(self):
        return self.get_request().json()
