import json
from config import FILE


def read_data():
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    vacancies = []
    for vacancy in data:
        vacancies.append(vacancy)
    return vacancies