import os
import shutil
import argparse

def parse_arguments():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за розширенням.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

def read_directory(directory):
    # Рекурсивне читання директорій
    files_to_copy = []
    try:
        for entry in os.scandir(directory):
            if entry.is_dir():
                files_to_copy.extend(read_directory(entry.path))
            elif entry.is_file():
                files_to_copy.append(entry.path)
    except Exception as e:
        print(f"Помилка при читанні директорії {directory}: {e}")
    return files_to_copy

def copy_files(files, dest_dir):
    # Копіювання файлів у відповідні піддиректорії на основі розширення файлів
    for file in files:
        try:
            file_extension = os.path.splitext(file)[1][1:]  # Отримати розширення файлу без крапки
            if not file_extension:
                file_extension = "no_extension"
            dest_path = os.path.join(dest_dir, file_extension)
            os.makedirs(dest_path, exist_ok=True)
            shutil.copy(file, dest_path)
        except Exception as e:
            print(f"Помилка при копіюванні файлу {file}: {e}")

def main():
    args = parse_arguments()
    source_dir = os.path.abspath(args.source_dir)
    dest_dir = os.path.abspath(args.dest_dir)

    print(f"Вихідна директорія: {source_dir}")
    print(f"Директорія призначення: {dest_dir}")

    if not os.path.exists(source_dir):
        print(f"Вихідна директорія {source_dir} не існує.")
        return

    files_to_copy = read_directory(source_dir)
    copy_files(files_to_copy, dest_dir)
    print(f"Файли скопійовані та відсортовані у {dest_dir}")

if __name__ == "__main__":
    main()