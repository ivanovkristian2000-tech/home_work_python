"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""
import os
import sys




if len(sys.argv) != 2:
    print("Использование: python task_26_01.py <путь>")
    sys.exit()

path = sys.argv[1]

if not os.path.isdir(path):
    print("Указанный путь не является директорией или не существует.")
    sys.exit()


items = os.listdir(path)

folders = []
files = []


for i in items:
    full_path = os.path.join(path, i)

    if os.path.isdir(full_path):
        folders.append(i)

    elif os.path.isfile(full_path):
        files.append(i)


print(f"Содержимое директории {path}")

print("Папки:")
if folders:
    print("- " + "\n- ".join(folders))
else:
    print("Папок нет")

print("Файлы:")
if files:
    print("- " + "\n- ".join(files))
else:
    print("Файлов нет")

