from .animal import Animal

class ThePet(Animal):
    """Базовый класс для домашних животных"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.tip = "Домашнее животное"

    def identify_the_animal_species(self):
        return self.tip

class Dog(ThePet):
    """Класс Собака"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.nov = "Собака"

    def identify_the_animal_species(self):
        return self.nov

class Cat(ThePet):
    """Класс Кошка"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.nov = "Кошка"

    def identify_the_animal_species(self):
        return self.nov

class Rooster(ThePet):
    """Класс Петух"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.nov = "Петух"

    def identify_the_animal_species(self):
        return self.nov