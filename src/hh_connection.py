from config import FILE
from src.vacancyAPI import VacancyAPI
from src.vacancies import Vacancy
import json
import requests


class GetHeadHunter(VacancyAPI, Vacancy):
    """
    Класс для получения вакансий с сайта hh.ru
    с наследованием от VacancyAPI, Vacancy
    """
    def __init__(self, name, top_n):
        """
        Создание экземпляра класса GetHeadHunter
        """
        super().__init__(name, top_n)
        self.top_n = top_n
        self.url = "https://api.hh.ru"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.top_n})"

    @property
    def get_vacancy(self):
        """
        Метод чтения вакансий с HH.ru
        :return: json
        """
        data = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name,
                                    'area': 113,
                                    'enable_snippets': "true",
                                    'only_with_salary': "true",
                                    'per_page': self.top_n}).json()
        return data

    def get_json(self):
        """
        Метод записи вакансий в файл
        :return: json
        """
        with open(FILE, "w", encoding="UTF-8") as file:
            file.write(json.dumps(self.get_vacancy, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    r = GetHeadHunter("python", 100)
    r.get_json
