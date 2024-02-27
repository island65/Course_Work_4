from src.input_forms import InputForm


class DebugUsersJson(InputForm):
    """
    Класс для отлавливания ошибок
    """
    salary = None
    city = None

    def user_input_int(self):
        """Проверка на наличие ошибок ввода
        :return: integer
        """
        self.salary = input(f"Введите минимальную заработную плату: ")
        if self.salary.isalpha():
            raise ValueError("Введите число")
        if self.salary == "":
            self.salary = 0
        return int(self.salary)

    def user_input_str(self):
        """Проверка на наличие ошибок ввода
        :return: string
        """
        self.city = input("Введите город: ").title().strip()
        # if self.city == "":
        #     raise ValueError("Запрос не может быть пустым")
        if self.city.isdigit():
            raise TypeError("Город не может быть числом")
        return self.city

if __name__ == '__main__':
    r = DebugUsersJson()
    print(r.user_input_str())