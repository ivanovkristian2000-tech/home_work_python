""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys




def find_files_with_extension(directory, extension):
    """Рекурсивно ищет файлы с заданным расширением."""
    found_files = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:

            if file_name.endswith(extension):
                full_path = os.path.join(dir_path, file_name)
                found_files.append(full_path)


    return found_files



if len(sys.argv) != 3:
    print("Использование: python task_26_02.py <путь> <расширение>")
    sys.exit()

directory = sys.argv[1]
extension = sys.argv[2]

if not os.path.isdir(directory):
    print("Указанный путь не является директорией или не существует.")
    sys.exit()

result = find_files_with_extension(directory, extension)

if result:
    print(f"Найдены файлы с расширением '{extension}'")
    for file in result:
        print(f"- {file}")
else:
    print(f"Файлы с расширением '{extension}' не найдены.")
    sys.exit()

user_input = input("\nВы хотите удалить эти файлы? (yes/no): ")

if user_input == 'yes':
    for file in result:
        os.remove(file)
    print("Удаление завершено.")
else:
    print("Удаление прервано.")








# # Предварительно создаём ненужные файлы для удаления
# files = [
#     'error.log',
#     'system.log',
#     'old.log',
#     'debug.log',
# ]
#
# for file in files:
#     with open(file, 'w') as f:
#         f.write("")