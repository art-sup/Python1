import json
import os

def write_order_to_json(item,quantity,price,buyer,date):
    dict_to_json = {
            "Item": item,
            "Quantity": quantity,
            "Price": price,
            "Buyer": buyer,
            "Date": date
    }
    filename=os.path.join("/Users/tema-/Documents/git/Python. Расширенный курс/Unit2/orders.json")
    with open(filename, 'w') as f_n:
        json.dump(dict_to_json, f_n,indent=4)

write_order_to_json('Boots',1,10.0,'Volkov',"21-12-2018")










with open('mes_example_write_2.json', 'w') as f_n:
    json.dump(dict_to_json, f_n)

with open('mes_example_write_2.json') as f_n:
    print(f_n.read())
