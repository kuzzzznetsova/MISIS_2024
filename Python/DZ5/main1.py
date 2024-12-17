def calculate_average_and_below_average(file_path):
    # Словарь для хранения студентов и их баллов
    students = {}

    # Чтение данных из файла
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            name, score = line.rsplit(' ', 1)  # Разделяем строку на имя и балл
            students[name] = int(score)  # Сохраняем в словаре

    # Вычисление среднего балла
    total_score = sum(students.values())
    number_of_students = len(students)
    average_score = total_score / number_of_students if number_of_students > 0 else 0

    # Вывод среднего балла
    print(f"Средний балл: {average_score:.2f}")

    # Список отстающих студентов (балл ниже среднего)
    below_average_students = [name for name, score in students.items() if score < average_score]

    # Вывод списка отстающих
    if below_average_students:
        print("Список отстающих студентов:")
        for student in below_average_students:
            print(student)
    else:
        print("Нет отстающих студентов.")

# Пример использования
file_path = 'students.txt'  # Укажите путь к вашему файлу
calculate_average_and_below_average(file_path)
