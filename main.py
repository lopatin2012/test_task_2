import json
from datetime import datetime
import os


def add_file_json_for_delete_in_list() -> None:
    """
    Находит все json файлы в папке со скриптом, и добавляем их в список.
    :return None:
    """
    files = os.listdir()
    files_for_delete = []
    for file_name in files:
        if file_name.endswith(".json"):
            with open(file_name, "r") as file:
                data = json.load(file)
                if "result" in data:
                    files_for_delete.append(file_name)
    delete_file_json_in_list(files_for_delete)


def delete_file_json_in_list(list_files: list) -> None:
    """
    Удаляет файлы в полученном списке.
    :param list_files:
    :return None:
    """
    for file in list_files:
        os.remove(file)


def button_test_1():
    """
    Выполнение тестового задания python №1.
    :return None:
    """
    add_file_json_for_delete_in_list()
    row = entry_data_field_1.get()
    if "(" not in row and ")" not in row:
        label_text_field_1_result.config(text="Результат задания №1:\nСкобки отсутствуют")
        save_result_in_json_file(False)
    else:
        result = checking_the_entered_brackets(row)
        label_text_field_1_result.config(text="Результат задания №1:\n" + str(result) + "\n")


def button_test_2():
    """
    Выполнение тестового задания python №2.
    :return None:
    """
    add_file_json_for_delete_in_list()
    row = entry_data_field_2.get()
    if row == "":
        result = 0
        label_text_field_2_result.config(text="Результат задания №2:\n" + str(result))
    else:
        result = max_counter_one_in_row(list(map(int, row.split(","))))
        label_text_field_2_result.config(text="Результат задания №2:\n" + str(result))


def save_result_in_json_file(result: bool | int) -> None:
    """
    Сохраняет булевую переменную с ключом result в текущую папку.
    Имя файла: текущая дата и время формата '%d.%m.%Y %H.%M'
    :param result:
    :return None:
    """
    format_file_name = datetime.now().strftime('%d.%m.%Y %H.%M')
    with open(f"{format_file_name}.json", "w", encoding="UTF-8") as file_json:
        json.dump({"result": result}, file_json)


def checking_the_entered_brackets(row: str):
    """
    Функция проверяет правильную последовательность скобок.
    Также проверяет был ли соблюден порядок.
    :return bool:
    Примеры:
    'фывафыа ыа ываф, (fdkgj()' => False
    'фываф (fdkgj())' => True
    """
    row = "".join(filter(lambda x: x in "()", row))
    while "()" in row:
        row = row.replace("()", "")

    add_file_json_for_delete_in_list()
    save_result_in_json_file(row == "")
    return row == ""


def max_counter_one_in_row(lst: list) -> int:
    """
    Нахождение максимального количества повторний цифры 1 в списке
    :param lst:
    :return int:
    """
    counter = 0
    lst_counters = []
    for symbol in lst:
        if symbol == 1:
            counter += 1
        else:
            lst_counters.append(counter)
            counter = 0
        lst_counters.append(counter)
    save_result_in_json_file(max(lst_counters))
    return max(lst_counters)

# Тестовые значения для задания №1
# checking_the_entered_brackets("фывафыа ыа ываф, (fdkgj()")
# checking_the_entered_brackets("фываф (fdkgj())")

# Тестовые значения для задания №2
# print(max_counter_one_in_row([0, 1, 0, 1, 1, 1, 0]))
# print(max_counter_one_in_row([0, 1, 1, 0, 1, 0]))


if __name__ == '__main__':
    from tkinter import Tk, Label, Entry, Button

    # UI
    root = Tk()
    root.title("Тестовые задания на python")
    root.geometry("400x400")

    # Задание №1
    label_text_field_1 = Label(text="Проверка скобок\n\nВведите строку")
    label_text_field_1.pack()
    entry_data_field_1 = Entry()
    entry_data_field_1.pack()
    button_field_1 = Button(text="Проверить строку", command=button_test_1)
    button_field_1.pack()
    label_text_field_1_result = Label(text="Результат задания №1:\n")
    label_text_field_1_result.pack()

    # Задание №2
    label_text_field_2 = Label(text="Проверка максимального повторения '1'\n\n"
                                    "Введите цифры 1 и 0 в произвольном порядке через запятую")
    label_text_field_2.pack()
    entry_data_field_2 = Entry()
    entry_data_field_2.pack()
    button_field_2 = Button(text="Проверить строку", command=button_test_2)
    button_field_2.pack()
    label_text_field_2_result = Label(text="Результат задания №2:")
    label_text_field_2_result.pack()

    root.mainloop()
