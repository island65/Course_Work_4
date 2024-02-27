class Vacancy:
    """
    Форма для класса GetHeadHunter
    """
    def __init__(self, name, page):
        self.__name = name
        self.__page = page

    @property
    def name(self):
        """
        Геттер для приватного аттрибута name
        """
        return self.__name

    @property
    def page(self):
        """
        Геттер для приватного аттрибута page
        """
        return self.__page

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name, self.__page})"
