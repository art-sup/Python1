import csv
import os
import re


#«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы»
#os_prod_list, os_name_list, os_code_list, os_type_list
#main_data
def get_value(my_line):
    re_pattern = r'^.*:\s*'
    return re.split(re_pattern,my_line)

def get_data():
    filepath="/Users/tema-/Documents/git/Python. Расширенный курс/Unit2/"
    main_data = [['Изготовитель системы', 'Название ОС', 'Тип системы', 'Код продукта']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in os.listdir(filepath):
        if file.endswith(".txt"):
            filename = os.path.join(filepath) + file
            try:
                with open(filename) as f_n:
                    for line in f_n:
                        if ('Изготовитель ОС' in line):
                            value_list = get_value(line)
                            os_prod_list.append(value_list[1].rstrip())
                        elif 'Название ОС' in line:
                            value_list = get_value(line)
                            os_name_list.append(value_list[1].rstrip())
                        elif 'Код продукта' in line:
                            value_list = get_value(line)
                            os_code_list.append(value_list[1].rstrip())
                        elif 'Тип системы' in line:
                            value_list = get_value(line)
                            os_type_list.append(value_list[1].rstrip())
                f_n.close()
            except FileNotFoundError:
                print(f'файл {filename} не найден')

    max_len = max(len(os_name_list),len(os_prod_list),len(os_type_list),len(os_code_list))
    for count in range(max_len):
        main_data_list=[]
        main_data_list.append(os_name_list[count])
        main_data_list.append(os_prod_list[count])
        main_data_list.append(os_type_list[count])
        main_data_list.append(os_code_list[count])
        main_data.append(main_data_list)

    return (main_data)

def write_to_csv(FILENAME):
    info = get_data()
    with open(FILENAME, 'w') as f_n:
        f_n_writer = csv.writer(f_n,quoting = csv.QUOTE_NONNUMERIC)
        for row in info:
            f_n_writer.writerow(row)
    f_n.close()

FILENAME = "/Users/tema-/Documents/git/Python. Расширенный курс/Unit2/info.csv"
write_to_csv(FILENAME)
