from binascii import Error
from .connector import DataBase

class TableBuilder:
    """Класс для создания таблиц базы данных"""
    def __init__(self):
        self.db = DataBase()

    def check_and_create_tables(self):
        """Проверяет, существуют ли таблицы"""
        connection = self.db.get_the_connection()
        if not connection:
            return False

        cursor = connection.cursor()
        
        try:
            # Таблица домашних животных
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS `ДомашниеЖивотные` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `имя` VARCHAR(100) NOT NULL,
                    `тип` VARCHAR(50) NOT NULL,
                    `дата_рождения` DATE NOT NULL,
                    `команды` TEXT,
                    `дата_создания` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)
            
            # Другие запросы создания таблиц...
            
            connection.commit()
            print("Все таблицы были успешно проверены и/или созданы")
            return True
            
        except Error as e:
            print(f"Ошибка проверки таблицы: {e}")
            return False
        finally:
            cursor.close()