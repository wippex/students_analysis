"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

sum_math = 0
sum_python = 0
sum_english = 0
best_average = 0
best_name = ""
count = 0

with open (INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        strip = line.strip("\n")
        split = strip.split(",")
        name = split[0]
        marks = [int(x) for x in split[1:]]
        math = marks[0]
        python = marks[1]
        english = marks[2]
        sum_math = sum_math + math
        sum_python = sum_python + python
        sum_english = sum_english + english
        count = count + 1

        average = sum(marks) / len(marks)

        if average > best_average:
            best_average = average
            best_name = name
average_math = sum_math / count
average_python= sum_python / count
average_english = sum_english / count


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
with open(OUTPUT_FILE, "w") as f:
    f.write("Середній бал по класу:\n")
    f.write(f"math: {average_math:.1f}\n")
    f.write(f"python: {average_python:.1f}\n")
    f.write(f"english: {average_english:.1f}\n")
    f.write("\n")
    f.write(f"Найкращий студент: {best_name} ({best_average:.1f})")

print("Середній бал по класу:")
print(f"math: {average_math:.1f}")
print(f"python: {average_python:.1f}")
print(f"english: {average_english:.1f}")
print()
print(f"Найкращий студент: {best_name} ({best_average:.1f})")

#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
