from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def get_request(self):
        pass
