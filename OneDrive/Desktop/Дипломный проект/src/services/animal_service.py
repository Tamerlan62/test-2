from src.database.connector import DataBase
from src.models.domestic_animals import Dog, Cat, Rooster
from src.models.pack_animals import Horse, Camel, Donkey
from datetime import datetime
from mysql.connector import Error # type: ignore

class AnimalServices:
    """Сервис для операций с животными"""
    def __init__(self):
        self.db = DataBase()

    def add_animal(self, animal):
        """Добавляет новое животное"""
        connection = self.db.get_the_connection()
        if not connection:
            return False

        cursor = connection.cursor()
        
        try:
            # Выберает правильную таблицу в зависимости от типа животного
            if isinstance(animal, (Dog, Cat, Rooster)):
                table = "ThePet"
            elif isinstance(animal, (Horse, Camel, Donkey)):
                table = "PackAnimal"
            else:
                print("Неизвестные виды животных")
                return False

            # Если есть команды, сойдиняет через запятую
            commands_str = ", ".join(animal.commands) if animal.commands else ""
            
            # Запрос на вставку в базу данных
            request = f"""
                INSERT INTO {table} (имя, тип, дата_рождения, команды)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(request, (animal.name, animal.identify_the_animal_species(), 
                                 animal.date_of_birth, commands_str))
            connection.commit()
            print(f"{animal.ad} успешно добавлено")
            return True
            
        except Error as e:
            print(f"Ошибка добавления животного: {e}")
            return False
        finally:
            cursor.close()

