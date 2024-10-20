from books_sdk import get_book_by_id, get_author

print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))

# Гипотеза 1: Неправильные скобки
# Способ проверки: методом клика пройтись по какой скобке
# Установленный факт: Все скоюки правильные
# Вывод: ()

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: print(get_author(get_book_by_id))
# Установленный факт: фцнкции отрабатывают
# Вывод: return book['author']

# Гипотеза 3: Проблема в типе данных, '1' должно быть числом
# Способ проверки: Удалил строку 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM'
# Код для проверки: print(get_author(get_book_by_id(1)))
# Установленный факт: Не верный аргумент для get_book_by_id
# Вывод: print(get_author(get_book_by_id(1)))

# Гипотеза 4: Проверить к ниги с другими id
# Способ проверки: Подстановка других id
# Код для проверки: print(get_author(get_book_by_id(10)))
# Установленный факт: Не верный аргумент для get_book_by_id
# Вывод: print(get_author(get_book_by_id(1)))

# Гипотеза 5: Аргументы перепутаны местами
# Способ проверки: поменял местами порядок аргументов ('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)
# Код для проверки: print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM', 1)))
# Установленный факт: Lело в порядке аргументов
# Вывод: Николай Гоголь
