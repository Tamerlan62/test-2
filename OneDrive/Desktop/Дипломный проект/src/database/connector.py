import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore
import os

class DataBase:
    """Класс для соединения с базой данных"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        """Подключение к базе данных"""
        try:
            self._connection = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST', 'mysql'),
                user=os.getenv('MYSQL_USER', 'root'),
                password=os.getenv('MYSQL_PASSWORD', 'rootparol'),
                database=os.getenv('MYSQL_DATABASE', 'Друзья_человека')
            )
            if self._connection.is_connected():
                print("Успешное подключение к базе данных")
                return self._connection
        except Error as e:
            print(f"Ошибка базы данных: {e}")
            return None

    def get_the_connection(self):
        """Возвращает активное соединение"""
        if self._connection is None or not self._connection.is_connected():
            self.connect()
        return self._connection

    def close_connection(self):
        """Закрывает соединение"""
        if self._connection and self._connection.is_connected():
            self._connection.close()
            print("Соединение с базой данных закрыто")