""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""
movies = "movies_to_watch.txt"




def remove_duplicates(filename: str) -> None:

    uniq_movies = f"unique_{filename}"
    uniq = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line not in uniq:
                uniq.append(line)

        with open(uniq_movies, 'w', encoding='utf-8') as w:
            w.writelines(uniq)




try:
    remove_duplicates(movies)

except FileNotFoundError as e:
    print("Ошибка: Не найден файл", e)
