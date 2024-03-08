from datetime import datetime


class Vacancy:
    def __init__(self, name, city, min_salary, requirement, responsibility, date):
        self.name = name
        self.city = city
        self.min_salary = min_salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.date = date

    @staticmethod
    def hh_data_validation(data):
        """
        Метод валидации данных и запись в список
        :return: list
        """
        validated_data = []
        for i in data['items']:
            if i['salary']['from'] is None:
                i['salary']['from'] = 0
            if i['published_at']:
                date = datetime.strptime(i['published_at'], '%Y-%m-%dT%H:%M:%S+%f')
                date_format = f"{date:%d.%m.%Y}"
            else:
                date_format = "--"
            validated_data.append({
                'name': i['name'],
                'city': i['area']['name'],
                'min_salary': i['salary']['from'],
                'requirement': i['snippet']['requirement'],
                'responsibility': i['snippet']['responsibility'],
                'date': date_format
            })
        return validated_data

    def __gt__(self, other):
        return int(self.min_salary) > int(other.min_salary)

    def __lt__(self, other):
        return int(self.min_salary) < int(other.min_salary)

    def __str__(self):
        return (f"Город: {self.city}\nДата публикации: {self.date}\n"
                f"Должность: {self.name}\nТребование: {self.requirement}\n"
                f"Ответственность: {self.responsibility}\nЗарплата: {self.min_salary}\n")
