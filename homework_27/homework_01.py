""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""
filename = "system_log.txt"
keyword = "error"
new_filename = f"{keyword}_{filename}"



def find_keyword(filename: str, keyword: str, new_filename: str) -> None:
    with open(filename, encoding="utf-8") as f:
        matched_lines = []
        for line in f:
            if keyword in line:
                matched_lines.append(line)
        if matched_lines:
            with open(new_filename, 'w', encoding="utf-8") as w:
                w.writelines(matched_lines)
        else:
            print("Совпадения не найдены.")



try:
    find_keyword(filename, keyword, new_filename)

except FileNotFoundError as e:
    print("Ошибка: Не найден файл", e)
