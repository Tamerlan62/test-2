from .animal import Animal

class PackAnimal(Animal):
    """Базовый класс для вьючных животных"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.type = "Вьючное животное"

    def identify_the_animal_species(self):
        return self.type

class Horse(PackAnimal):
    """Класс Лошадь"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.type = "Лошадь"

    def identify_the_animal_species(self):
        return self.type

class Camel(PackAnimal):
    """Класс Верблюд"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.type = "Верблюд"

    def identify_the_animal_species(self):
        return self.type

class Donkey(PackAnimal):
    """Класс Осел"""
    def __init__(self, name, date_of_birth, commands=None):
        super().__init__(name, date_of_birth, commands)
        self.type = "Осел"

    def identify_the_animal_species(self):
        return self.type