# src/main.py Добавьте это в начало файла
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Прочий импорт (используйте абсолютный импорт)
from src.services.animal_service import AnimalServices
from src.database.connector import DataBase
from src.database.setup import TableBuilder
from src.utils.counter import Counter
from src.models.domestic_animals import Dog, Cat, Rooster
from src.models.pack_animals import Horse, Camel, Donkey
from datetime import datetime

def main_menu():
    """Показывает главное меню"""
    print("\n=== Система регистрации животных ===")
    print("1. Добавить новое животное")
    print("2. Показать команды животных")
    print("3. Научите животное новой команде")
    print("4. Уберите верблюдов и соедините лошадей и ослов")
    print("5. Создайте текущий график животных")
    print("6. Объединить все таблицы")
    print("7. Выполнение команд Linux")
    print("0. Выход")

def add_animal():
    """Меню для добовление новых животных"""
    print("\nВыберите тип животного:")
    print("1. Собака")
    print("2. Кошка")
    print("3. Петух")
    print("4. Лошадь")
    print("5. Верблюд")
    print("6. Осоль")
    print("0. Назад")

def main():
    # Создать базу данных
    table_builder = TableBuilder()
    table_builder.check_and_create_tables()
    
    animal_services = AnimalServices()
    counter = Counter()

    while True:
        main_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            with counter:
                add_animal()
                type_selection = input("Ваш выбор: ")
                
                if type_selection == "0":
                    continue
                    
                name = input("Имя животного: ")
                date_of_birth = input("Дата рождения(ГГ-ММ-ДД): ")
                
                try:
                    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
                    commands = input("Команды (разделите через запятую): ").split(",")
                    commands = [command.strip() for command in commands if command.strip()]
                    
                    animal_species = {
                        "1": Dog,
                        "2": Cat,
                        "3": Rooster,
                        "4": Horse,
                        "5": Camel,
                        "6": Donkey
                    }
                    
                    if type_selection in animal_species:
                        animal = animal_species[type_selection](name, date_of_birth, commands)
                        animal_services.add_animal(animal)
                        print(f"Добавлено новое животное. Общее количество: {counter.increases()}")
                    else:
                        print("Неправильный выбор!")
                        
                except ValueError:
                    print("Неверный формат даты! Введите в формате ГГ-ММ-ДД.")
        
        # Другие опции меню...
        
        elif choice == "0":
            break
            
        else:
            print("Неправильный выбор! Попробуйте еще раз.")

    # Закройте соединение.
    db = DataBase()
    db.close_connection()

if __name__ == "__main__":
    main()