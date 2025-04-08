from datetime import date
from abc import ABC, abstractmethod

class Animal(ABC):
    """Базовый класс для животных"""
    def __init__(self, name, date_of_birth, commands=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.commands = commands or []

    def add_command(self, command):
        """Обучение животного новой команде"""
        self.commands.append(command)

    def calculate_age(self):
        """Вычисляет возраст животного"""
        toDay = date.today()
        age = toDay.year - self.date_of_birth.year - ((toDay.month, toDay.day) < 
              (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def age_in_months(self):
        """Вычисляет возраст животного в месяцах"""
        toDay = date.today()
        months = (toDay.year - self.date_of_birth.year) * 12 + toDay.month - self.date_of_birth.month
        if toDay.day < self.date_of_birth.day:
            months -= 1
        return months

    @abstractmethod
    def specify_type(self):
        """Определяет вид животного"""
        pass