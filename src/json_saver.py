from config import FILE
import json


class JsonSaver:
    """
    Класс для чтения и сохранения в json файл
    """
    def write_data_json(self, data):
        """
        Метод записи вакансий в файл
        :return: json
        """
        with open(FILE, "w", encoding="UTF-8") as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
