import csv
import os
import re


#«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы»
#os_prod_list, os_name_list, os_code_list, os_type_list
#main_data
def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in os.listdir("/Users/tema-/Documents/git/Python. Расширенный курс/Unit2"):
        if file.endswith(".txt"):
            filename = os.path.join("/Users/tema-/Documents/git/Python. Расширенный курс/Unit2/") + file
            with open(filename) as f_n:
                for row in f_n:
                    result_os_prod = re.search(r'(?<=Изготовитель системы:[\s+]).*?(?=\n)',string=row)
                    result_os_name = re.search(r'(?<=Название ОС:[\s+]).*?(?=\n)', string=row)
                    result_os_code = re.search(r'(?<=Код продукта:[\s+]).*?(?=\n)', string=row)
                    result_os_type = re.search(r'(?<=Тип системы:[\s+]).*?(?=\n)', string=row)
                    if (result_os_prod != None):
                        os_prod_list.append(result_os_prod[0])
                    else:
                        if (result_os_name != None):
                            os_name_list.append(result_os_name[0])
                        else:
                            if (result_os_code != None):
                                os_code_list.append(result_os_code[0])
                            else:
                                if (result_os_type != None):
                                    os_type_list.append(result_os_type[0])

    # print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)
    f_n.close()
    main_data = {"Изготовитель системы":os_prod_list, "Название ОС":os_name_list, "Код продукта":os_code_list, "Тип системы":os_type_list}
    return (main_data.copy())

def write_to_csv(FILENAME):
    with open(FILENAME, 'w') as f_n:
        info = get_data()
        print(info.values())
        columns = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
        f_n_writer = csv.DictWriter(f_n,fieldnames=columns)
        f_n_writer.writeheader()
        f_n_writer.writerows(info)
    f_n.close()

FILENAME = "/Users/tema-/Documents/git/Python. Расширенный курс/Unit2/info.csv"
write_to_csv(FILENAME)
