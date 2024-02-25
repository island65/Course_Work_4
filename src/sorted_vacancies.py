import json
from datetime import datetime
from config import FILE
from pprint import pprint


class Sortedvacancies():
    def __init__(self):
        self.hh_sorted = []
        self.date_format = None

    @property
    def hh_sorted_vacancies(self):
        with open(FILE, encoding="UTF-8") as file:
            content = json.load(file)
        for i in content['items']:
            if i['salary']['from'] is None:
                i['salary']['from'] = 0
            if i['salary']['from'] is None:
                i['salary']['from'] = 0
            if i['published_at']:
                date = datetime.strptime(i['published_at'], '%Y-%m-%dT%H:%M:%S+%f')
                self.date_format = f"{date:%d.%m.%Y}"
            self.hh_sorted.append({
                'name': i['name'],
                'city': i['area']['name'],
                'min_salary': i['salary']['from'],
                'max_salary': i['salary']['to'],
                'requirement': i['snippet']['requirement'],
                'responsibility': i['snippet']['responsibility'],
                'date': self.date_format
            })
        return self.hh_sorted


if __name__ == '__main__':
    r = Sortedvacancies()
    pprint(r.hh_sorted_vacancies)
    