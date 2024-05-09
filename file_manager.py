import os
import shutil
from pathlib import Path
import sys

"""

Запуск програми виконується через термінал.

Вкажіть через пробіл: 

1. Шлях до програми (обов'язково): <file_manager.py>
2. Шлях до вихідної директорії (обов'язково): <вихідна_директорія> 
3. Шлях до директорії призначення (не обов'язково): <директорія_призначення>

"""

# Функція, яка рекурсивно копіює файли з вихідної директорії в нову, сортуючи їх по розширенню
def sort_files(source_dir, dest_dir=None):

    # Абсолютний шлях до нової директорії
    if not dest_dir:
        dest_dir = os.path.join(os.path.abspath(source_dir), "dist")
    else:
        dest_dir = os.path.join(os.path.abspath(source_dir), dest_dir)
        Path(dest_dir).mkdir(parents=True, exist_ok=True)

    for entry in os.scandir(source_dir):
        if entry.is_dir():
            sort_files(entry.path, dest_dir)
        elif entry.is_file():
            # Отримання розширення файлу
            filename, extension = os.path.splitext(entry.name)

            # Створення піддиректорії для розширення, якщо її не існує
            ext_dir = Path(dest_dir, extension[1:])
            ext_dir.mkdir(parents=True, exist_ok=True)

            # Копіювання файлу до піддиректорії або в директорію призначення
            if not os.path.dirname(entry.path) == source_dir:
                shutil.copy(entry.path, ext_dir)
            else:
                shutil.copy(entry.path, os.path.join(dest_dir, extension[1:]))


if __name__ == "__main__":
    # Обробка аргументів командного рядка
    if len(sys.argv) < 2:
        print("Недостатньо аргументів. Вкажіть через пробіл:\n"
              "1. Шлях до програми (обов'язково): <file_manager.py>\n"
              "2. Шлях до вихідної директорії (обов'язково): <вихідна_директорія>\n"
              "3. Шлях до директорії призначення (не обов'язково): <директорія_призначення>")
        exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) >= 3 else None

    # Перевірка існування вихідної директорії
    if not os.path.exists(source_dir):
        print(f"Вихідна директорія '{source_dir}' не існує.")
        exit(1)

    # Запуск сортування файлів
    sort_files(source_dir, dest_dir)

    if dest_dir:
        print(f"Файли успішно відсортовані та скопійовані в директорію '{dest_dir}'.")
    else:
        print("Файли успішно відсортовані та скопійовані в директорію 'dist'.")
