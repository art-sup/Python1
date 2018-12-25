import yaml

def save_yaml():
    action_list = ['msg_1',
              'msg_2',
              'msg_3']

    data_to_yaml = {'key1':action_list, 'key2':23, 'key3':{1:'\u04E0',2:'\u14DF',3:'\u0A07',4:'£'}}

    with open('data_write.yaml', 'w',encoding='utf-8') as f_n:
        yaml.dump(data_to_yaml, f_n,default_flow_style=False,allow_unicode=True)
        f_n.close()

def read_yaml():
    with open('data_write.yaml','r',encoding='utf-8') as f_n:
        value = yaml.load(f_n)
        f_n.close()
        return value

save_yaml()
print(read_yaml())