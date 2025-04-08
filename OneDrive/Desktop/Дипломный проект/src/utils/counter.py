from contextlib import contextmanager
import warnings

class Counter:
    """Класс Счетчик"""
    def __init__(self):
        self._value = 0
        self._is_open = False

    def increases(self):
        """Увеличивает значение на 1 единицу"""
        if not self._is_open:
            raise ResourceWarning("Ресурс счетчика не открыт!")
        self._value += 1
        return self._value

    def __enter__(self):
        """Вход в менеджер контекста"""
        self._is_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """вывод для менеджера контекста"""
        self._is_open = False
        if exc_type is not None:
            warnings.warn(f"Произошла ошибка: {exc_val}")
        return True

    def current_value(self):
        """Возвращает текущий номер"""
        return self._value